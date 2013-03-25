import sys
import os
from xml.dom import minidom

class Luigi:

  def __init__(self):

		self.s_scp_name = []
		self.s_scp_time = []
		self.s_scp_error_num = []

		self.f_scp_name = []
		self.f_scp_time = []
		self.f_scp_error_num = []
		self.f_scp_error_msg = []

	def read_file(self, rpt_obj):
		if(rpt_obj is not None):
			rpt_obj.seek(0)
			print rpt_obj.read()

	def pick_fail_scp_out(self, file_path):

		if(os.path.exists(file_path)):

			rpt_obj = minidom.parse(file_path)

			try:
				ele_arr = rpt_obj.getElementsByTagName('Script')

				if(ele_arr is not None):

					for ele in ele_arr:
						if(ele.getAttribute('name') != '' and ele.getAttribute('errors') != '0'):
							f_scp_name = ele.getAttribute('name')
							f_scp_time = ele.getAttribute('time')
							f_scp_error_msg = ele.getAttribute('message')

							self.f_scp_name.append(str(f_scp_name))
							self.f_scp_time.append(f_scp_time)
							self.f_scp_error_num.append(1)
							self.f_scp_error_msg.append(f_scp_error_msg)
			except:
				print "oops: When Louise try to get success scripts, he got failed"
				sys.exit(0)

	def pick_succ_scp_out(self, file_path):

		if(os.path.exists(file_path)):

			rpt_obj = minidom.parse(file_path)
			try:
				ele_arr = rpt_obj.getElementsByTagName('Script')
				
				if(ele_arr is not None):
					
					for ele in ele_arr:
						if(ele.getAttribute('name') != '' and ele.getAttribute('errors') == '0'):
							s_scp_name = ele.getAttribute('name')
							s_scp_time = ele.getAttribute('time') 

							self.s_scp_name.append(str(s_scp_name))
							self.s_scp_time.append(s_scp_time)
							self.s_scp_error_num.append(0)
			except:
				print "oops: When Louise try to get success scripts, he got some troubles"
				sys.exit(0)

