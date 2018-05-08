#!/usr/bin/python
# vim: noet sw=4 ts=4

import	os
from	setuptools	import	setup

name    = 'anon-ip'
dirname = 'anon_ip'
version = '0.0.0rc3'

def	read( fn ):
	with open(
		os.path.join(
			os.path.dirname( __file__ ),
			fn
		)
	) as f:
		return f.read()

try:
	os.makedirs( dirname )
except:
	pass

vfile = os.path.join(
	dirname,
	'version.py'
)
with open( vfile, 'w' ) as f:
	print >>f, "Version = '{0}'".format( version )

setup(
	name		 = name,
	version		 = version,
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
	url              = "http://666.666.666.666:666",
	packages         = [
		dirname,
		# 'tests',
	],
	long_description = read( 'README.md' ),
	classifiers      =[
		"Development Status :: 0 - Broken",
		"Topic :: Utilities",
		"License :: OSI Approved :: MIT",
	],
	scripts = [
		'anon-ip',
	],
)
