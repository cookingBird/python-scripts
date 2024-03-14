from file_reader import read_files;
from request import request_test;
from excel import write_dict_array_to_excel;

input = "./input"



def handle_entry(key,value):
	fail = [];
	rows = value;
	for item in rows:
		res = request_test(item['record_details'],item);
		if res['success'] == False:
			fail.append(res['payload']);
	return fail;

json_files = read_files(input)
for file in json_files:
	info = file['info']
	data = file['data']
	fail_result = [];
	for key, value in data.items():
		fail_result = handle_entry(key, value)
	print('fail length: ',len(fail_result))
	write_dict_array_to_excel(fail_result, './output/' + info['base_name'] + '.xlsx')
