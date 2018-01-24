#!/usr/bin/python3
#Shayna Anderson-Hill
#Script to write a function that draws a grid
#01-22-2018

plus = '+'
minus = '-'
space = ' '
line = '|'

#Naive Answer
print('Part One')
print(plus, (minus+space)*4,plus, (minus+space)*4,plus)
print(line, space*8, line, space*8, line)
print(line, space*8, line, space*8, line)
print(line, space*8, line, space*8, line)
print(line, space*8, line, space*8, line)
print(plus, (minus+space)*4,plus, (minus+space)*4,plus)
print(line, space*8, line, space*8, line)
print(line, space*8, line, space*8, line)
print(line, space*8, line, space*8, line)
print(line, space*8, line, space*8, line)
print(plus, (minus+space)*4,plus, (minus+space)*4,plus)

#Create function to print grid customized by input value n

def horizontals(n, columns=2):
    print(plus, (minus+space)*(n-1) + minus, plus, (minus + space)*(n-1)+
            minus,plus)

def verticals(n):
    for i in range(n):
        print(line, space*((n*2)-1), line, space*((n*2)-1), line)

print('Part 2:')

def print_standard_grid(n, size = 2):
    horizontals(n)
    verticals(n)
    horizontals(n)
    verticals(n)
    horizontals(n)

units = int(input('How many units?'))
print_standard_grid(units)

print('Part3:')
units = int(input('How many units?'))
rows = int(input('How many rows?'))
columns = int(input('How many columns?'))

def column(columns, units):
    for i in range(columns):
        print(plus, (minus+space)*(units-1) + minus, end=' ')
    print(plus)

def row(rows, units, columns):
    for row in range(units): 
        for i in range(columns):
            print(line, space*((units*2)-1), end=' ')
        print(line)

def print_custom_grid(units, rows, columns):
    for i in range(rows): 
        column(columns, units)
        row(rows, units, columns)
    column(columns, units)

print_custom_grid(units,rows,columns)

