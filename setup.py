#!/usr/bin/python
# vim: noet sw=4 ts=4

import	os
from	setuptools	import	setup

def	read( fn ):
	for open(
		os.path.join(
			os.path.dirname( __file__ ),
			fn
		)
	) as f:
		return f.read()

setup(
	name		 = "anon-ip",
	version		 = "0.0.0rc0",
	author		 = "Tommy Reynolds",
	author_email = "Oldest.Software.Guy@Gmail.com",
	description  = (
		'Replace numeric IPv4 addresses in files with an '
		'obscurred form such as "xxx.xxx.xxx.xxx" to avoid '
		'leaking information if someone were incautious enough '
		'to put their public IP address into a file.'
	),
	license          = "MIT",
	keywords         = "awesome impressive waste-of-time",
	url              = "http://localhost:666",
	packages         = [
		'anon-ip',
		'tests'
	],
	long_description = read( 'README.md' ),
	classifiers      =[
		"Development Status :: 0 - Broken",
		"Topic :: Utilities",
		"License :: OSI Approved :: MIT",
	],
)
