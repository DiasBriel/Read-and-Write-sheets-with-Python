from rw_sheet import read_sheets, write_final_result

SPREADSHEET_ID = '1msCoeLoQj8IVgm-KwXcfMabj0llxGktVT6RJbGC68II'

cels_to_read = "engenharia_de_software!A2:H2"
data_result = read_sheets(cels_to_read, SPREADSHEET_ID)
print(data_result)

where_to_write = "engenharia_de_software!G4:H27"
data_to_write = [['Hello'],['Hello'],['Hello'],['Hello'],['Hello'],]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)
