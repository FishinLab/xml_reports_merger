import os
import sys
from Mario import Mario
from Louise import Louise

  
if sys.argv[1] == '-h' or sys.argv[1] == '--help':
	
	print """
	-h: (--help) 			display this help page;

	-i: (--input_files)		input 2 files, the first one is merger, and the second one is mergee

	-o: (--output_file) 	the output xml report's path
	"""
	
elif sys.argv[1] == '-i' or sys.argv[1] == 'input_files':
		
	if sys.argv[4] == '-o' or sys.argv[4] == '--output_file':

		merger = sys.argv[2]
		mergee = sys.argv[3]
		result = sys.argv[5]

		if os.path.exists(merger) and os.path.exists(mergee):
				
			m = Mario()
			m.load_merger_file(merger)
			m.load_mergee_file(mergee)

			succ_scp_name = m.get_succ_script_node(merger)
			fail_scp_name = m.get_fail_script_node(mergee)

			m.merge_xml(m.merger_tree , m.mergee_tree, succ_scp_name, fail_scp_name)

			m.generate_xml_tree(m.result_tree, result)
	
		else:
			print "oops: the input files does not exists"
			exit(0)
else:
	print """
	-h: (--help) 			display this help page;

	-i: (--input_files)		input 2 files, the first one is merger, and the second one is mergee

	-o: (--output_file) 	the output xml report's path
	"""


