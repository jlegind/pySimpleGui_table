import PySimpleGUI as sg
import logging

logging.basicConfig(filename='example.log',level=logging.DEBUG)
logging.info("trying to log to file")


records = [[1, 'box 1', 'Delta grevillea'], [2, 'shelf 2', 'Oxalis delta'], [3, 'box 3', 'Rosa rugosa']]
header = ['id', 'storage', 'taxon_name']

tibble = sg.Table(records, headings=header, enable_events=True, num_rows=5, key="_tibble_" )
layout = [
    [tibble]
]

window = sg.Window('Table demo', layout)


def makeRecord(row, mkHeader):
    # returns a dict record from the header list and the row 2D list
    logging.info('mkRec row: %s', str(row))
    mkRecord = dict(zip(mkHeader, row[0]))
    return mkRecord


while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break

    if event == '_tibble_':
        data_selected = [records[row] for row in values[event]]
        logging.info('data_selected: %s', data_selected )
        record = makeRecord(data_selected, header)
        print(record)
        logging.info("the record ID is:: %d", record['id'])

