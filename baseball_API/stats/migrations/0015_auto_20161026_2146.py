# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-26 21:46
from __future__ import unicode_literals

from django.db import migrations

import csv

def add_master_data(apps, schema_editor):
    Master = apps.get_model("stats", "Master")
    with open('Master.csv') as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            Master.objects.create(player=row["playerID"], birthYear=row["birthYear"],
                birthMonth=row["birthMonth"], birthDay=row["birthDay"], birthCountry=row["birthCountry"],
                birthState=row["birthState"], birthCity=row["birthCity"], deathYear=row['deathYear'],
                deathMonth=row['deathMonth'], deathDay=row['deathDay'],deathState=row['deathState'],
                deathCountry=row['deathCountry'],
                deathCity=row['deathCity'], nameFirst=row['nameFirst'], nameLast=row['nameLast'],
                nameGiven=row['nameGiven'], weight=row['weight'], height=row['height'], bats=row['bats'],
                throws=row['throws'], debut=row['debut'], finalGame=['finalGame'], retroID=['retroID'],
                bbrefID=row['bbrefID'])


def add_batting_data(apps, schema_editor):
    Master = apps.get_model("stats", "Master")
    Batting = apps.get_model("stats", "Batting")
    with open('Batting.csv') as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            print(row)
            player = Master.objects.get(player=row["playerID"])
            Batting.objects.create(player=player, year=row["yearID"], stint=row['stint'], team=row["teamID"],
            league=row['lgID'], games=row['G'], at_bats=row['AB'], runs=row['R'],
            hits=row['H'], doubles=row["2B"], triples=row['3B'], home_runs=row['HR'],
            rbi=row['RBI'], stolen_bases=row['SB'], caught_stealing=row['CS'],
            walks=row['BB'], strikeouts=row['SO'], intentional_walks=row['IBB'],
            hit_by_pitch=row['HBP'], sac_hits=row['SH'], sac_flies=['SF'], double_plays=row['GIDP'])

    raise Exception('asfasdfasdfasdfasdfasdfasdfasdf')


def add_fielding_data(apps, schema_editor):
    Master = apps.get_model("stats", "Master")
    with open('Fielding.csv') as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            print(row)
            player = Master.objects.get(player=row["playerID"])
            Fielding.objects.create(player=player, year=row["yearID"], stint=row['stint'], team=row["teamID"],
            league=row['lgID'], position=row['Pos'], games=row['G'], games_started=row['GS'],
            innOuts=row['InnOuts'], put_outs=row['PO'], assists=row['A'], double_plays=row['DP'],
            passed_balls=row['PB'], wild_pitches=row['WP'], stolen_bases=row['SB'],
            caught_stealing=row['CS'], zone=row['ZR'] )



class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0014_auto_20161026_2146'),
    ]

    operations = [
    #migrations.RunPython(add_batting_data),
    #migrations.RunPython(add_master_data)
    #migrations.RunPython(add_fielding_data)
    ]
