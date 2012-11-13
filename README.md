HAUS-start installs a script which allows the easy creation of Django
projects and applications.  Based on the red-start project from RED interactive.

How to use
==========

Creating a project
------------------


    $ git clone git@github.com:MadeInHaus/haus-start.git
    ./haus-start/bin/haus-start ProjectName


Following hasn't been tested:

    pip install git+https://github.com/madeinhaus/haus-start.git
    haus-start ProjectName



This will use the default project template, which includes
HAUS's [django-template](https://github.com/madeinhaus/django-template).

Running a project
-----------------

    vagrant up
    fab syncdb
    fab runserver

How does it work
================

Creating a project from a template
----------------------------------

Running haus-start does three simple things:

1. Creates a new folder called `<folder_name>`.
2. Copies in that folder all the files included in the project template folder. This can be specified with the `--template-dir` option; the default is `templates/project/django-template`.
3. If a file called `haus_start_settings.py` is present in that folder, and if it contains a function called `after_copy`, then that file is loaded and that function executed.

As an example, in the case of the django-template project template, the [after_copy function](https://github.com/madeinhaus/haus-start/blob/master/haus_start/templates/project/django-template/haus_start_settings.py) downloads an HTML5 boilerplate from GitHub, prompts the user for some variables and substitutes them in the template. This is just an example, other project templates can perform any other operation.


Creating a new project template
-----------------------------------

To add a new project template to haus-start, simply add it in the `templates` folder, under `project`. If you need to perform extra actions after the files have been copied, add a file called `haus_start_settings.py` with an `after_copy` function (take a look at existing templates).

Finally, to use the newly created template, just indicate its path as the `--template-dir` option, for instance:

    haus-start --template-dir=/your/custom/template new_example


```
$ git clone git@github.com:MadeInHaus/haus-start.git
$ ./haus-start/bin/haus-start BestProject
$ cd BestProject/
```
```
$ vagrant up

[default] Importing base box 'precise64'...
[default] The guest additions on this VM do not match the install version of
VirtualBox! This may cause things such as forwarded ports, shared
folders, and more to not work properly. If any of those things fail on
this machine, please update the guest additions and repackage the
box.

Guest Additions Version: 4.2.0
VirtualBox Version: 4.1.16
[default] Matching MAC address for NAT networking...
[default] Clearing any previously set forwarded ports...
[default] Forwarding ports...
[default] -- 22 => 2222 (adapter 1)
[default] -- 8000 => 8080 (adapter 1)
[default] Creating shared folders metadata...
[default] Clearing any previously set network interfaces...
[default] Booting VM...
[default] Waiting for VM to boot. This can take a few minutes.
[default] VM booted and ready for use!
[default] Mounting shared folders...
[default] -- v-root: /vagrant
[default] -- project: /var/www
[default] -- manifests: /tmp/vagrant-puppet/manifests
[default] -- v-pp-m0: /tmp/vagrant-puppet/modules-0
[default] Running provisioner: Vagrant::Provisioners::Puppet...
[default] Running Puppet with /tmp/vagrant-puppet/manifests/app.pp...
stdin: is not a tty
notice: /Stage[first]/App::Apt-get-update/Exec[apt-get update]/returns: executed successfully
notice: /Stage[main]/App::Postgresql/Package[libpq-dev]/ensure: ensure changed 'purged' to 'present'
notice: /Stage[main]/App::Git/Package[git]/ensure: created
notice: /Stage[main]/App::Rabbitmq/Package[rabbitmq-server]/ensure: ensure changed 'purged' to 'present'
notice: /Stage[main]/App::Postgresql/Package[postgresql]/ensure: ensure changed 'purged' to 'present'
notice: /Stage[main]/App::Postgresql/Exec[createpguser]/returns: executed successfully
notice: /Stage[main]/App::Python/Package[python-pip]/ensure: ensure changed 'purged' to 'present'
notice: /Stage[main]/App::Python/Package[python-dev]/ensure: ensure changed 'purged' to 'present'
notice: /Stage[main]/App::Postgresql/Exec[createpgdb]/returns: executed successfully
notice: /Stage[main]/App::Redis/Package[redis-server]/ensure: ensure changed 'purged' to 'present'
notice: /Stage[main]/App::Pipreq/Exec[pip-install]/returns: executed successfully
notice: /Stage[main]/App::Redis/File[redis.conf]/content: content changed '{md5}30bd132aa06130b11c045f9d05abe1ab' to '{md5}289f7308b748cb88b938f78a69224b83'
notice: /Stage[main]/App::Redis/Service[redis-server]: Triggered 'refresh' from 1 events
notice: /Stage[main]/App::Vim/Package[vim]/ensure: ensure changed 'purged' to 'present'
notice: Finished catalog run in 699.21 seconds
```
```

$ fab syncdb

[vagrant@127.0.0.1:2222] out: You just installed Django's auth system, which means you don't have any superusers defined.
[vagrant@127.0.0.1:2222] out: Would you like to create one now? (yes/no): yes
[vagrant@127.0.0.1:2222] out: (0.001) SELECT "auth_user"."id", "auth_user"."username", "auth_user"."first_name", "auth_user"."last_name", "auth_user"."email", "auth_user"."password", "auth_user"."is_staff", "auth_user"."is_active", "auth_user"."is_superuser", "auth_user"."last_login", "auth_user"."date_joined" FROM "auth_user" WHERE "auth_user"."username" = 'vagrant' ; args=('vagrant',)
[vagrant@127.0.0.1:2222] out: Username (leave blank to use 'vagrant'): admin
[vagrant@127.0.0.1:2222] out: (0.001) SELECT "auth_user"."id", "auth_user"."username", "auth_user"."first_name", "auth_user"."last_name", "auth_user"."email", "auth_user"."password", "auth_user"."is_staff", "auth_user"."is_active", "auth_user"."is_superuser", "auth_user"."last_login", "auth_user"."date_joined" FROM "auth_user" WHERE "auth_user"."username" = 'admin' ; args=('admin',)
[vagrant@127.0.0.1:2222] out: E-mail address: joshua_t@madeinhaus.com
[vagrant@127.0.0.1:2222] out: Password: 
[vagrant@127.0.0.1:2222] out: Password (again): 
```
```


$ fab runserver 

[vagrant@127.0.0.1:2222] Executing task 'runserver'
[vagrant@127.0.0.1:2222] run: ps ax | grep [p]ython | awk '{ print $1 }' | xargs kill -9
[vagrant@127.0.0.1:2222] out: Usage:
[vagrant@127.0.0.1:2222] out:   kill pid ...              Send SIGTERM to every process listed.
[vagrant@127.0.0.1:2222] out:   kill signal pid ...       Send a signal to every process listed.
[vagrant@127.0.0.1:2222] out:   kill -s signal pid ...    Send a signal to every process listed.
[vagrant@127.0.0.1:2222] out:   kill -l                   List all signal names.
[vagrant@127.0.0.1:2222] out:   kill -L                   List all signal names in a nice table.
[vagrant@127.0.0.1:2222] out:   kill -l signal            Convert between signal numbers and names.
[vagrant@127.0.0.1:2222] out: 


Warning: run() received nonzero return code 123 while executing 'ps ax | grep [p]ython | awk '{ print $1 }' | xargs kill -9'!

[vagrant@127.0.0.1:2222] run: python ./manage.py runserver [::]:8000
[vagrant@127.0.0.1:2222] out: Validating models...
[vagrant@127.0.0.1:2222] out: 
[vagrant@127.0.0.1:2222] out: 0 errors found
[vagrant@127.0.0.1:2222] out: Django version 1.4.2, using settings 'settings'
[vagrant@127.0.0.1:2222] out: Development server is running at http://[::]:8000/
[vagrant@127.0.0.1:2222] out: Quit the server with CONTROL-C.
[vagrant@127.0.0.1:2222] out: 
[2]+  Stopped                 fab runserver

$ bg
[2]+ fab runserver &
```
```

$ curl 127.0.0.1:8080

<!DOCTYPE html>
<html lang="en">
<head>
  <meta http-equiv="content-type" content="text/html; charset=utf-8">
  <title>Page not found at /</title>
  <meta name="robots" content="NONE,NOARCHIVE">
  <style type="text/css">
    html * { padding:0; margin:0; }
    body * { padding:10px 20px; }
    body * * { padding:0; }
    body { font:small sans-serif; background:#eee; }
    body>div { border-bottom:1px solid #ddd; }
    h1 { font-weight:normal; margin-bottom:.4em; }
    h1 span { font-size:60%; color:#666; font-weight:normal; }
    table { border:none; border-collapse: collapse; width:100%; }
    td, th { vertical-align:top; padding:2px 3px; }
    th { width:12em; text-align:right; color:#666; padding-right:.5em; }
    #info { background:#f6f6f6; }
    #info ol { margin: 0.5em 4em; }
    #info ol li { font-family: monospace; }
    #summary { background: #ffc; }
    #explanation { background:#eee; border-bottom: 0px none; }
  </style>
</head>
<body>
  <div id="summary">
    <h1>Page not found <span>(404)</span></h1>
    <table class="meta">
      <tr>
        <th>Request Method:</th>
        <td>GET</td>
      </tr>
      <tr>
        <th>Request URL:</th>
      <td>http://127.0.0.1:8080/</td>
      </tr>
    </table>
  </div>
  <div id="info">
    
      <p>
      Using the URLconf defined in <code>urls</code>,
      Django tried these URL patterns, in this order:
      </p>
      <ol>
        
          <li>
            
                ^grappelli/
                
            
          </li>
        
          <li>
            
                ^admin/doc/
                
            
          </li>
        
          <li>
            
                ^admin/
                
            
          </li>
        
          <li>
            
                ^static\/(?P&lt;path&gt;.*)$
                
            
          </li>
        
      </ol>
      <p>The current URL, <code></code>, didn't match any of these.</p>
    
  </div>

  <div id="explanation">
    <p>
      You're seeing this error because you have <code>DEBUG = True</code> in
      your Django settings file. Change that to <code>False</code>, and Django
      will display a standard 404 page.
    </p>
  </div>
</body>
</html>
Not Found: /
[vagrant@127.0.0.1:2222] out: [13/Nov/2012 07:09:12] "GET / HTTP/1.1" 404 2237
[vagrant@127.0.0.1:2222] out:
```