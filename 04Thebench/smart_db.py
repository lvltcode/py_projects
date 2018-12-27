#!/usr/bin/env python
# coding=UTF-8
import sys
import json
import csv


def get_query(file):
    with open(file, "r") as f:
        json_file = json.load(f)
    return json_file


def load_data():
    data = []
    lines = sys.stdin.readlines()
    for line in lines:
        data.append(line.strip('\n').split(','))
    return data


def sort_result(result, order, select_field):
    if order == 'age':
        result.sort(key=lambda x: int(x[select_field.index(order)]))
    else:
        result.sort(key=lambda x: x[select_field.index(order)])
    return result


def get_mode_condition(query):
    if 'where_or' in query.keys():
        return 'where_or'
    elif 'where_and' in query.keys():
        return 'where_and'
    else:
        return None


def extract_condition(condition, line, ordered_query):
    try:
        # take left condition if "left" is first_letter first_name
        if 'first_letter' in condition['left']:
            # take first_name
            field = condition['left'].split(' ')[1]
            # take out first letter name e.g: H, M
            left = line[ordered_query.index(field)][0]
            # take second condition e.g: T, M
            right = condition['right']
        else:
            # else check condition gender, age
            field = condition['left']
            # check if field = age
            if field == ordered_query[3]:
                # take age type int
                left = int(line[3])
                # take condition age type int
                right = int(condition['right'])
            elif field == ordered_query[4]:
                left = line[ordered_query.index(condition['left'])]
                if condition['right'] == 'M':
                    right = 'male'
                else:
                    right = 'female'
            else:
                # take gender
                left = line[ordered_query.index(condition['left'])]
                right = condition['right']
        return left, right
    except TypeError:
        return None, None


def get_info(mode, line, query, ordered_query):
    if mode is None:
        pass
    else:
        conditions = query[mode]
        if len(conditions) == 1:
            condition_1 = conditions[0]
            left1, right1 = extract_condition(condition_1, line, ordered_query)
            return left1, right1, None, None
        elif len(conditions) == 2:
            condition_1 = conditions[0]
            condition_2 = conditions[1]
            left1, right1 = extract_condition(condition_1, line, ordered_query)
            left2, right2 = extract_condition(condition_2, line, ordered_query)
            return left1, right1, left2, right2, condition_1, condition_2


def compare(condition, a, b):
    if condition['op'] == '=':
        # if left's condition = right's
        if a == b:
            return True
    elif condition['op'] == '>':
        # if left's condition > right's
        if a > b:
            return True
    elif condition['op'] == '<':
        # if left's condition < right's
        if a < b:
            return True
    elif condition['op'] == '!=':
        if a != b:
            return True


def filter_one_query(query, data, select_field):
    ordered_query = ['first_name',
                     'last_name',
                     'username',
                     'age',
                     'gender',
                     'city']
    mode = get_mode_condition(query)
    result = []
    for line in data:
        if mode is None:
            temp = []
            for item in select_field:
                temp.append(line[ordered_query.index(item)])
            result.append(temp)
        else:
            l1, r1, l2, r2, con1, con2 = get_info(mode, line,
                                                  query, ordered_query)
            if mode == 'where_and':
                if compare(con1, l1, r1) and compare(con2, l2, r2):
                    temp = []
                    for item in select_field:
                        temp.append(line[ordered_query.index(item)])
                    result.append(temp)
            elif mode == 'where_or':
                if compare(con1, l1, r1) or compare(con2, l2, r2):
                    temp = []
                    for item in select_field:
                        temp.append(line[ordered_query.index(item)])
                    result.append(temp)
    return result


def main():
    queries = get_query(sys.argv[-1])
    data = load_data()
    for query in queries:
        select_field = query['select'].split(', ')
        result = filter_one_query(query, data, select_field)
        if 'order' in query.keys():
            result = sort_result(result, query['order'], select_field)
        print(result)


if __name__ == '__main__':
    main()
