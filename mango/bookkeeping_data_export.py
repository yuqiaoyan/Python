from vr.common.config import get_configuration
from vr.common.utils.mongo import RetryingConnection
from vr.common.bookkeeping import BookkeepingFactory
from time import sleep
from datetime import datetime, timedelta

class GetExportedBKData(object):
	def get_bk_data(self, data_start_time):

		local_config = get_configuration()
		bookkeeping_engine = RetryingConnection(local_config.DB_CONFIG['bookkeeping']['db_host'])[local_config.DB_CONFIG['bookkeeping']['db_name']]
		bookkeeping_factory = BookkeepingFactory(bookkeeping_engine)
		db_book_current_p = bookkeeping_engine['book_current_p']

		bookkeeping_data = []
		bk_id_list = []
		
		for bkid in db_book_current_p.find({},{'_id':1}):
			bk_id_list.append(bkid['_id'])
			#print bkid['_id']
		
		for bk_id in bk_id_list:
			for bk_entry in bookkeeping_factory.get_bookkeeping(bk_id).get_last_k(6000):
				
				if bk_entry['attime'] > data_start_time and bk_entry['attime'] < (data_start_time + timedelta(hours = 12)) :
					bookkeeping_data.append(bk_entry)
		
		return bookkeeping_data
	
	def output_kb_csv(self, bookkeeping_data, append_to_name):
		
		output_filename = "./data_files/bk_stats_dump_" + str(append_to_name) + ".csv"
		f = open(output_filename,"w")
		f.write('bookkeeping_id\tattime\ttime\tcount\n')
		for bkid in bookkeeping_data:
		#	for bkid in bkids:
				
			b_id = bkid.get('bookkeeping_id','no_id')
			attime = bkid.get('attime','no_attime')
			time = bkid.get('time','no_time')
			count = bkid.get('count','no_count')
				
			f.write(str(b_id) + '\t' + str(attime) + '\t' + str(time) + '\t' + str(count) + '\n' )
		
if __name__ == "__main__":
		
	start_time = datetime.utcnow()
	print "Started Program at: ", start_time
	
	data_start_time = start_time - timedelta(hours = 12)
	
	file_name_counter = 0
	
	while True:
		
		start_export_time = 0
		
		export_data = GetExportedBKData()
		bk_data = export_data.get_bk_data(data_start_time)
		export_data.output_kb_csv(bk_data, file_name_counter)
		
		print "Exported data slice: from ",data_start_time," until ", (data_start_time + timedelta(hours = 12))
		# the next data start time (12 hour slices of data)
		data_start_time = data_start_time + timedelta(hours = 12)
		file_name_counter += 1
		print "Current Time: ",datetime.utcnow()
		
		# sleep until the next data slice is ready to be read
		sleep_for_time = (data_start_time + timedelta(hours = 12)) - datetime.utcnow()
		sleep_for_time =  sleep_for_time.days * 86400 + sleep_for_time.seconds + 60
		
		
		sleep(sleep_for_time)
		
	
	
	