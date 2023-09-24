#!/usr/bin/env bash
#Let’s practice using Puppet to make changes to our configuration fil

file {'/etc/ssh/ssh_config':
	ensure => present,
content =>"

	#ssh client configuration
	host*
	IdentityFile ~/.ssh/school
	PasswordAuthentication no
	",
}
