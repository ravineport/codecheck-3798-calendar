#!/usr/bin/env python3
import string

class NewCalendar:

    def __init__(self, args):
        self.days_in_year = int(args[0])
        self.days_in_month = int(args[1])
        self.days_in_week = int(args[2])
        self.days_of_the_week_list = list(string.ascii_uppercase)[:self.days_in_week]
        self.month_in_year = int(self.days_in_year / self.days_in_month)
        self.rest_days_in_year = self.days_in_year % self.days_in_month

    def input_validation(self, input_ymd):
        '''
        入力されたYYYY-MM-DDは有効？
        '''
        if input_ymd[1] > self.month_in_year + 1 or input_ymd[2] > self.days_in_month:
            return False
        if input_ymd[1] == self.month_in_year + 1:
            return self.is_leap_year(input_ymd[0])
        return True

    def days_until_the_year(self, input_year):
        '''
        input_yearまでの日数
        '''
        days_until_input_year = input_year * self.month_in_year * self.days_in_month + self.leap_days(input_year)
        return days_until_input_year

    def leap_days(self, input_year):
        '''
        input_year終了までのうるう月の日数
        '''
        all_stack_days = (input_year) * self.rest_days_in_year
        ans_days = all_stack_days - (all_stack_days % self.days_in_month)
        return ans_days

    def is_leap_year(self, input_year):
        '''
        input_yearはうるう年？
        '''
        ld = self.leap_days(input_year)
        stack_days = 0
        for i in range(1, input_year):
            stack_days += self.rest_days_in_year
            if stack_days >= self.days_in_month:
                stack_days -= self.days_in_month

        stack_days += self.rest_days_in_year
        if stack_days >= self.days_in_month:
            return True
        else:
            return False


    def calc_day_of_the_week(self, date):
        '''
        YYYY-MM-DDは何曜日？
        '''
        input_ymd = list(map(int, date.split('-')))
        if not self.input_validation(input_ymd):
            return '-1'
        days_until_last_year = self.days_until_the_year(input_ymd[0] - 1) if input_ymd[0] != 1 else 0
        days_in_the_year = (input_ymd[1] - 1) * self.days_in_month + input_ymd[2]
        days = days_until_last_year + days_in_the_year
        return self.days_of_the_week_list[days % self.days_in_week - 1]


def main(argv):
    nc = NewCalendar(argv[:3])
    print(nc.calc_day_of_the_week(argv[3]))
