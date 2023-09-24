#!/usr/bin/env bash
#Let’s practice using Puppet to make changes to our configuration fil

file {'/etc/ssh/ssh_config':
  ensure => present,
}

file_line {'Turn off passwd auth':
  path  => '/etc/ssh/ssh_config',
  line  => 'PasswordAuthentication no',
  match => '^#PasswordAuthentication',
}

file_line {'Declare identity file':
  path  => '/etc/ssh/ssh_config',
  line  => 'IdentitiyFile~/.ssh/school',
  match => '^#IdentityFile',
}
