#!/usr/bin/python
# vim: noet sw=4 ts=4

import	argparse
import	sys
import	os
import	re
import	re

try:
	from version import Version
except:
	Version = '0.0.0rc0'

class	AnonIP( object ):

	def	__init__( self ):
		self.opts = dict({
			'show_ip_map' : False,
			'obs_offset'  : 0,
		}),
		self.alphabet = 'abcdefhijklmnopqrstvwxyz' + 'ABCDEFHIJKLMNOPQRSTVWXYZ'
		self.Nalphabet = len( self.alphabet )
		return

	def	process( self, name ):
		if os.path.isdir( name ):
			for rootdir, dirs, entries in os.walk( name ):
				for d in sorted( dirs ):
					_ = map(
						lambda dn : self.process(
							os.path.join(
								rootdir,
								dn
							),
							sorted( dirs )
						)
					)
		elif os.path.isfile( name ):
			with open( name ) as f:
				self.do_file( f )
		else:
			pass
		return

	def	obscure( self, mo ):
		ipaddr = mo.group( 0 )
		if ipaddr not in self.ip_map:
			pos = (self.which + self.opts.obs_offset) % self.Nalphabet
			c = self.alphabet[ pos ] * 3
			self.which += 1
			obscured = '.'.join(
				[ c ] * 4
			)
			self.ip_map[ ipaddr ] = obscured
		return self.ip_map[ ipaddr ]

	def	do_file( self, f = sys.stdin ):
		self.which = 0
		octet = r'[0-9]{1,3}'
		pattern = r'[.]'.join( [ octet ] * 4 )
		self.ip_map = dict()
		for line in f:
			print re.sub( pattern, self.obscure, line.rstrip() )
		if self.opts.show_ip_map:
			print
			print
			title = 'Anonamization IP Map'
			print title
			print '=' * len( title )
			print
			fmt = '{0:15}  {1:15}'
			subtitle = fmt.format( 'Obscurred', 'Original' )
			print subtitle
			print '-' * len( subtitle )
			for k in sorted( self.ip_map, key = lambda k : self.ip_map[k] ):
				print fmt.format( self.ip_map[ k ], k )

		return

	def	process( self, name ):
		if os.path.isfile( name ):
			with open( name ) as f:
				self.do_file( f )
		elif os.path.isdir( name ):
			for rootdir, dirs, names in os.walk( name ):
				for n in sorted( names ):
					fn = os.path.join(
						rootdir,
						n
					)
					self.process( fn )
				for d in sorted( dirs ):
					fn = os.path.join(
						rootdir,
						d
					)
					self.process( fn )
		else:
			pass
		return

	def	main( self ):
		prog = os.path.splitext(
			os.path.basename( sys.argv[ 0 ] )
		)[0]
		if prog == '__init__':
			prog = 'anon-ip'
		p = argparse.ArgumentParser(
			prog        = prog,
			description = '''\
				Replace any numeric IP addresses with symbolic
				charater-based values.
			'''
		)
		p.add_argument(
			'-a',
			'--alphabet',
			metavar = 'CHARS',
			dest    = 'alphabet',
			default = None,
			help    = 'choose from these charaters, in this order',
		)
		p.add_argument(
			'-m',
			'--map',
			dest   = 'show_ip_map',
			action = 'store_true',
			help   = 'show IP mapping table',
		)
		p.add_argument(
			'-O',
			'--offset',
			dest    = 'obs_offset',
			type    = int,
			metavar = 'N',
			default = 0,
			help    = 'pick obscuring characters later',
		)
		p.add_argument(
			'-o',
			'--out',
			dest    = 'ofile',
			default = None,
			help    = 'output to here instead of stdout',
		)
		p.add_argument(
			'-v',
			'--version',
			action  = 'version',
			version = Version,
			help    = '{0} v{1}'.format( prog, Version ),
		)
		p.add_argument(
			'names',
#			dest    = 'names',
			metavar = 'FILE',
			nargs   = '*',
			default = [],
			help    = 'file or directory, else stdin',
		)
		self.opts = p.parse_args()
		if self.opts.ofile:
			sys.stdout = open( self.opts.ofile, 'w' )
		if self.opts.alphabet:
			self.alphabet  = self.opts.alphabet
			self.Nalphabet = len( self.alphabet )
		if len( self.opts.names ) == 0:
			self.do_file()
		else:
			for name in self.opts.names:
				self.process( name )
		return 0

if __name__ == '__main__':
	exit( AnonIP().main() )
