# -*- coding: utf-8 -*-

"""Main module."""

import csv

import arrow
from ics import Calendar, Event


c = Calendar()


def export(inputfile, outputfile):
    with open(inputfile, encoding="utf8") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")

        for (start_date, start_time, end_date, end_time, title, place) in csvreader:
            if not start_date:
                start_date = end_date
            try:
                start = arrow.get(start_date + ' ' + start_time, 'D.M.YYYY H:m')
            except arrow.parser.ParserError:
                start = arrow.get(start_date + ' ' + start_time, 'D.M.YYYY H')
            start = start.replace(tzinfo='Europe/Zurich')
            try:
                end = arrow.get(end_date + ' ' + end_time, 'D.M.YYYY H:m')
            except arrow.parser.ParserError:
                end = arrow.get(end_date + ' ' + end_time, 'D.M.YYYY H')
            end = end.replace(tzinfo='Europe/Zurich')
            e = Event(name=title, begin=start, end=end, location=place)
            c.events.add(e)

    with open(outputfile, 'w') as output:
        output.writelines(c)
