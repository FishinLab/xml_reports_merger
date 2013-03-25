import os
import sys
from Luigi import Luigi
from xml.etree import ElementTree

class Mario:
  """
	
	"""

	def __init__(self):
		self.merger_tree = ElementTree.ElementTree()
		self.mergee_tree = ElementTree.ElementTree()
		self.merger_root = ElementTree.Element(None)
		self.mergee_root = ElementTree.Element(None)
		self.result_tree = ElementTree.ElementTree()

	def load_merger_file(self, merger_path):

		if(os.path.exists(merger_path)):
			merger_et = ElementTree.parse(merger_path)
			self.merger_tree = merger_et

	def load_mergee_file(self, mergee_path):
		
		if(os.path.exists(mergee_path)):
			mergee_et = ElementTree.parse(mergee_path)
			self.mergee_tree = mergee_et

	def get_merger_root(self, merger_et):
		self.merger_root = merger_et.getroot()

	def get_mergee_root(self, mergee_et):
		self.mergee_root = mergee_et.getroot()

	def get_fail_script_node(self, mergee_path):

		Luigi_obj = Luigi()
		Luigi_obj.pick_fail_scp_out(mergee_path)
		
		if(Louise_obj.f_scp_name is not None):
			return Louise_obj.f_scp_name
	
	def get_succ_script_node(self, merger_path):

		Luigi_obj = Luigi()
		Luigi_obj.pick_succ_scp_out(merger_path)
		
		if(Louise_obj.s_scp_name is not None):
			return Louise_obj.s_scp_name

	def merge_xml(self, merger_tree, mergee_tree, succ_scp_name, fail_scp_name):
	
		merger_root = merger_tree.getroot() 
		mergee_root = mergee_tree.getroot()

		tmp_removed_rec = []
		patt = '/Group'
		
		i = 1;
		while(i < 10 ): 

			pattern = patt * i
			parent_path = 'Scripts' + pattern 
			find_path = parent_path + '/Script'
			flag_obj_list = mergee_root.findall('Scripts' + pattern + '/Script')
			
			if(0 != len(flag_obj_list)):
				parents = mergee_root.findall(parent_path)

				for parent in parents:
					c = 0
					while(c < len(parent._children)):
						scp = parent._children[c]

						if 'Script' == scp.tag and 'File' in scp.attrib.keys():
							replace_scp_name = scp.attrib['File']

							if (replace_scp_name in succ_scp_name and replace_scp_name in fail_scp_name):
								tmp_removed_rec.append(replace_scp_name)
								parent.remove(scp)
								if c != 0:
									c = c - 1
								else:
									c = 0
						c = c + 1

					for scp in merger_root.findall(find_path):
						if 'Script' == scp.tag:
							insert_scp_name = scp.attrib['File']
						
							if(insert_scp_name in tmp_removed_rec):
								parent.insert(-1, scp)

				ele_arr = mergee_root.findall('Results' + pattern + '/Script')

				for ele in ele_arr:
					if 'name' in ele.attrib.keys() and 'message' in ele.attrib.keys():
						if ele.attrib['name'] in tmp_removed_rec and ele.attrib['errors'] != 0:
							ele.attrib['errors'] = '0'
							ele.attrib.pop('message')
				
				ele_arr = mergee_root.findall('Shutdown/Message')

				for ele in ele_arr:
					if ele.attrib['Type'] == 'Error':
						ele.attrib['Message'] = '0 scriipt(s) failed'
						ele.attrib['Type'] = 'Verification'
				
				ele_arr = mergee_root.findall('Results' + pattern + '/Summary')

				for ele in ele_arr:
					ele.attrib['errors'] = '0'
				
				ele_arr = mergee_root.findall('Results' + pattern + '/Script')

				for ele in ele_arr:
					if 'name' in ele.attrib.keys():
						if ele.attrib['name'] in tmp_removed_rec and ele.attrib['errors'] != '0':
							ele.attrib['errors'] = '0'
							ele.attrib.pop('message')
			i = i + 1	
						
		self.result_tree = mergee_tree

		for tmp in tmp_removed_rec:
			print tmp
			
	def generate_xml_tree(self, result_tree, output_path):
		
		if(os.path.exists(output_path)):
			print "oops: Mario found that the output file already exists"
			sys.exit(0)
		else:
			self.result_tree.write(output_path)


