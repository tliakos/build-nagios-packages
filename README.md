Packages the following projects into RPMs:

* [nagios-apache](http://github.com/jasonhancock/nagios-apache)
* [nagios-cpu](http://github.com/jasonhancock/nagios-cpu)
* [nagios-elasticsearch](http://github.com/jasonhancock/nagios-elasticsearch)
* [nagios-html-email](http://github.com/jasonhancock/nagios-html-email)
* [nagios-memory](http://github.com/jasonhancock/nagios-memory)
* [nagios-mysql](http://github.com/jasonhancock/nagios-mysql)
* [nagios-puppet](http://github.com/jasonhancock/nagios-puppet)
* [nagios-redis](http://github.com/jasonhancock/nagios-redis)

To build the RPM, you need to have docker installed, then run:
```
make
```

This will build a Docker container, then build everyting inside the container.

Two RPMs will be generated:

* nagios-plugins-hancock: The plugins to be installed on the edge servers
* nagios-plugins-hancock-pnp4nagios: The pnp4nagios configurations to be installed on the Nagios server
