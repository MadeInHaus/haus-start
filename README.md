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
Cloning into 'haus-start'...
remote: Counting objects: 57, done.
remote: Compressing objects: 100% (41/41), done.
remote: Total 57 (delta 15), reused 47 (delta 5)
Receiving objects: 100% (57/57), 8.69 KiB, done.
Resolving deltas: 100% (15/15), done.
(django-template)[joshua@StigmergicProductions:~/work/haus/t (master)]
$ ./haus-start/bin/haus-start BestProject
Initializing django-template submodule
Submodule 'haus_start/templates/project/django-template' (git@github.com:MadeInHaus/django-template.git) registered for path 'haus_start/templates/project/django-template'
Cloning into 'haus_start/templates/project/django-template'...
remote: Counting objects: 220, done.
remote: Compressing objects: 100% (129/129), done.
remote: Total 220 (delta 76), reused 215 (delta 71)
Receiving objects: 100% (220/220), 47.96 KiB, done.
Resolving deltas: 100% (76/76), done.
Submodule path 'haus_start/templates/project/django-template': checked out 'c96b95597fc315c08e74d6353a173eecf683eba8'
django-template submodule updated

Initialized empty Git repository in /Users/joshua/work/haus/t/BestProject/.git/
PROJECT NAME [Django Project]: Best Project
ADMIN EMAIL [cmsadmin@madeinhaus.com]: 
(django-template)[joshua@StigmergicProductions:~/work/haus/t (master)]
$ ls
BestProject haus-start
(django-template)[joshua@StigmergicProductions:~/work/haus/t (master)]
$ cd BestProject/
(django-template)[joshua@StigmergicProductions:~/work/haus/t/BestProject (master)]
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
(django-template)[joshua@StigmergicProductions:~/work/haus/t/BestProject (master)]
$ fab syncdb
[vagrant@127.0.0.1:2222] Executing task 'syncdb'
[vagrant@127.0.0.1:2222] run: python ./manage.py syncdb
[vagrant@127.0.0.1:2222] out: (0.053) 
[vagrant@127.0.0.1:2222] out:             SELECT c.relname
[vagrant@127.0.0.1:2222] out:             FROM pg_catalog.pg_class c
[vagrant@127.0.0.1:2222] out:             LEFT JOIN pg_catalog.pg_namespace n ON n.oid = c.relnamespace
[vagrant@127.0.0.1:2222] out:             WHERE c.relkind IN ('r', 'v', '')
[vagrant@127.0.0.1:2222] out:                 AND n.nspname NOT IN ('pg_catalog', 'pg_toast')
[vagrant@127.0.0.1:2222] out:                 AND pg_catalog.pg_table_is_visible(c.oid); args=()
[vagrant@127.0.0.1:2222] out: Creating tables ...
[vagrant@127.0.0.1:2222] out: Creating table django_admin_log
[vagrant@127.0.0.1:2222] out: (0.076) CREATE TABLE "django_admin_log" (
[vagrant@127.0.0.1:2222] out:     "id" serial NOT NULL PRIMARY KEY,
[vagrant@127.0.0.1:2222] out:     "action_time" timestamp with time zone NOT NULL,
[vagrant@127.0.0.1:2222] out:     "user_id" integer NOT NULL,
[vagrant@127.0.0.1:2222] out:     "content_type_id" integer,
[vagrant@127.0.0.1:2222] out:     "object_id" text,
[vagrant@127.0.0.1:2222] out:     "object_repr" varchar(200) NOT NULL,
[vagrant@127.0.0.1:2222] out:     "action_flag" smallint CHECK ("action_flag" >= 0) NOT NULL,
[vagrant@127.0.0.1:2222] out:     "change_message" text NOT NULL
[vagrant@127.0.0.1:2222] out: )
[vagrant@127.0.0.1:2222] out: ;; args=()
[vagrant@127.0.0.1:2222] out: Creating table auth_permission
[vagrant@127.0.0.1:2222] out: (0.004) CREATE TABLE "auth_permission" (
[vagrant@127.0.0.1:2222] out:     "id" serial NOT NULL PRIMARY KEY,
[vagrant@127.0.0.1:2222] out:     "name" varchar(50) NOT NULL,
[vagrant@127.0.0.1:2222] out:     "content_type_id" integer NOT NULL,
[vagrant@127.0.0.1:2222] out:     "codename" varchar(100) NOT NULL,
[vagrant@127.0.0.1:2222] out:     UNIQUE ("content_type_id", "codename")
[vagrant@127.0.0.1:2222] out: )
[vagrant@127.0.0.1:2222] out: ;; args=()
[vagrant@127.0.0.1:2222] out: Creating table auth_group_permissions
[vagrant@127.0.0.1:2222] out: (0.031) CREATE TABLE "auth_group_permissions" (
[vagrant@127.0.0.1:2222] out:     "id" serial NOT NULL PRIMARY KEY,
[vagrant@127.0.0.1:2222] out:     "group_id" integer NOT NULL,
[vagrant@127.0.0.1:2222] out:     "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED,
[vagrant@127.0.0.1:2222] out:     UNIQUE ("group_id", "permission_id")
[vagrant@127.0.0.1:2222] out: )
[vagrant@127.0.0.1:2222] out: ;; args=()
[vagrant@127.0.0.1:2222] out: Creating table auth_group
[vagrant@127.0.0.1:2222] out: (0.004) CREATE TABLE "auth_group" (
[vagrant@127.0.0.1:2222] out:     "id" serial NOT NULL PRIMARY KEY,
[vagrant@127.0.0.1:2222] out:     "name" varchar(80) NOT NULL UNIQUE
[vagrant@127.0.0.1:2222] out: )
[vagrant@127.0.0.1:2222] out: ;; args=()
[vagrant@127.0.0.1:2222] out: (0.004) ALTER TABLE "auth_group_permissions" ADD CONSTRAINT "group_id_refs_id_3cea63fe" FOREIGN KEY ("group_id") REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED;; args=()
[vagrant@127.0.0.1:2222] out: Creating table auth_user_user_permissions
[vagrant@127.0.0.1:2222] out: (0.005) CREATE TABLE "auth_user_user_permissions" (
[vagrant@127.0.0.1:2222] out:     "id" serial NOT NULL PRIMARY KEY,
[vagrant@127.0.0.1:2222] out:     "user_id" integer NOT NULL,
[vagrant@127.0.0.1:2222] out:     "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED,
[vagrant@127.0.0.1:2222] out:     UNIQUE ("user_id", "permission_id")
[vagrant@127.0.0.1:2222] out: )
[vagrant@127.0.0.1:2222] out: ;; args=()
[vagrant@127.0.0.1:2222] out: Creating table auth_user_groups
[vagrant@127.0.0.1:2222] out: (0.005) CREATE TABLE "auth_user_groups" (
[vagrant@127.0.0.1:2222] out:     "id" serial NOT NULL PRIMARY KEY,
[vagrant@127.0.0.1:2222] out:     "user_id" integer NOT NULL,
[vagrant@127.0.0.1:2222] out:     "group_id" integer NOT NULL REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED,
[vagrant@127.0.0.1:2222] out:     UNIQUE ("user_id", "group_id")
[vagrant@127.0.0.1:2222] out: )
[vagrant@127.0.0.1:2222] out: ;; args=()
[vagrant@127.0.0.1:2222] out: Creating table auth_user
[vagrant@127.0.0.1:2222] out: (0.004) CREATE TABLE "auth_user" (
[vagrant@127.0.0.1:2222] out:     "id" serial NOT NULL PRIMARY KEY,
[vagrant@127.0.0.1:2222] out:     "username" varchar(30) NOT NULL UNIQUE,
[vagrant@127.0.0.1:2222] out:     "first_name" varchar(30) NOT NULL,
[vagrant@127.0.0.1:2222] out:     "last_name" varchar(30) NOT NULL,
[vagrant@127.0.0.1:2222] out:     "email" varchar(75) NOT NULL,
[vagrant@127.0.0.1:2222] out:     "password" varchar(128) NOT NULL,
[vagrant@127.0.0.1:2222] out:     "is_staff" boolean NOT NULL,
[vagrant@127.0.0.1:2222] out:     "is_active" boolean NOT NULL,
[vagrant@127.0.0.1:2222] out:     "is_superuser" boolean NOT NULL,
[vagrant@127.0.0.1:2222] out:     "last_login" timestamp with time zone NOT NULL,
[vagrant@127.0.0.1:2222] out:     "date_joined" timestamp with time zone NOT NULL
[vagrant@127.0.0.1:2222] out: )
[vagrant@127.0.0.1:2222] out: ;; args=()
[vagrant@127.0.0.1:2222] out: (0.001) ALTER TABLE "django_admin_log" ADD CONSTRAINT "user_id_refs_id_c8665aa" FOREIGN KEY ("user_id") REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED;; args=()
[vagrant@127.0.0.1:2222] out: (0.001) ALTER TABLE "auth_user_user_permissions" ADD CONSTRAINT "user_id_refs_id_f2045483" FOREIGN KEY ("user_id") REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED;; args=()
[vagrant@127.0.0.1:2222] out: (0.001) ALTER TABLE "auth_user_groups" ADD CONSTRAINT "user_id_refs_id_831107f1" FOREIGN KEY ("user_id") REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED;; args=()
[vagrant@127.0.0.1:2222] out: Creating table django_content_type
[vagrant@127.0.0.1:2222] out: (0.004) CREATE TABLE "django_content_type" (
[vagrant@127.0.0.1:2222] out:     "id" serial NOT NULL PRIMARY KEY,
[vagrant@127.0.0.1:2222] out:     "name" varchar(100) NOT NULL,
[vagrant@127.0.0.1:2222] out:     "app_label" varchar(100) NOT NULL,
[vagrant@127.0.0.1:2222] out:     "model" varchar(100) NOT NULL,
[vagrant@127.0.0.1:2222] out:     UNIQUE ("app_label", "model")
[vagrant@127.0.0.1:2222] out: )
[vagrant@127.0.0.1:2222] out: ;; args=()
[vagrant@127.0.0.1:2222] out: (0.002) ALTER TABLE "django_admin_log" ADD CONSTRAINT "content_type_id_refs_id_288599e6" FOREIGN KEY ("content_type_id") REFERENCES "django_content_type" ("id") DEFERRABLE INITIALLY DEFERRED;; args=()
[vagrant@127.0.0.1:2222] out: (0.001) ALTER TABLE "auth_permission" ADD CONSTRAINT "content_type_id_refs_id_728de91f" FOREIGN KEY ("content_type_id") REFERENCES "django_content_type" ("id") DEFERRABLE INITIALLY DEFERRED;; args=()
[vagrant@127.0.0.1:2222] out: Creating table django_session
[vagrant@127.0.0.1:2222] out: (0.004) CREATE TABLE "django_session" (
[vagrant@127.0.0.1:2222] out:     "session_key" varchar(40) NOT NULL PRIMARY KEY,
[vagrant@127.0.0.1:2222] out:     "session_data" text NOT NULL,
[vagrant@127.0.0.1:2222] out:     "expire_date" timestamp with time zone NOT NULL
[vagrant@127.0.0.1:2222] out: )
[vagrant@127.0.0.1:2222] out: ;; args=()
[vagrant@127.0.0.1:2222] out: Creating table tastypie_apiaccess
[vagrant@127.0.0.1:2222] out: (0.003) CREATE TABLE "tastypie_apiaccess" (
[vagrant@127.0.0.1:2222] out:     "id" serial NOT NULL PRIMARY KEY,
[vagrant@127.0.0.1:2222] out:     "identifier" varchar(255) NOT NULL,
[vagrant@127.0.0.1:2222] out:     "url" varchar(255) NOT NULL,
[vagrant@127.0.0.1:2222] out:     "request_method" varchar(10) NOT NULL,
[vagrant@127.0.0.1:2222] out:     "accessed" integer CHECK ("accessed" >= 0) NOT NULL
[vagrant@127.0.0.1:2222] out: )
[vagrant@127.0.0.1:2222] out: ;; args=()
[vagrant@127.0.0.1:2222] out: Creating table tastypie_apikey
[vagrant@127.0.0.1:2222] out: (0.004) CREATE TABLE "tastypie_apikey" (
[vagrant@127.0.0.1:2222] out:     "id" serial NOT NULL PRIMARY KEY,
[vagrant@127.0.0.1:2222] out:     "user_id" integer NOT NULL UNIQUE REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED,
[vagrant@127.0.0.1:2222] out:     "key" varchar(256) NOT NULL,
[vagrant@127.0.0.1:2222] out:     "created" timestamp with time zone NOT NULL
[vagrant@127.0.0.1:2222] out: )
[vagrant@127.0.0.1:2222] out: ;; args=()
[vagrant@127.0.0.1:2222] out: (0.001) SELECT "django_content_type"."id", "django_content_type"."name", "django_content_type"."app_label", "django_content_type"."model" FROM "django_content_type" WHERE ("django_content_type"."model" = 'logentry'  AND "django_content_type"."app_label" = 'admin' ); args=('logentry', 'admin')
[vagrant@127.0.0.1:2222] out: (0.000) SAVEPOINT s139976396412672_x1; args=()
[vagrant@127.0.0.1:2222] out: (0.001) INSERT INTO "django_content_type" ("name", "app_label", "model") VALUES ('log entry', 'admin', 'logentry') RETURNING "django_content_type"."id"; args=(u'log entry', 'admin', 'logentry')
[vagrant@127.0.0.1:2222] out: (0.001) SELECT "auth_permission"."content_type_id", "auth_permission"."codename" FROM "auth_permission" INNER JOIN "django_content_type" ON ("auth_permission"."content_type_id" = "django_content_type"."id") WHERE "auth_permission"."content_type_id" IN (1) ORDER BY "django_content_type"."app_label" ASC, "django_content_type"."model" ASC, "auth_permission"."codename" ASC; args=(1,)
[vagrant@127.0.0.1:2222] out: (0.001) INSERT INTO "auth_permission" ("name", "content_type_id", "codename") VALUES ('Can add log entry', 1, 'add_logentry'), ('Can change log entry', 1, 'change_logentry'), ('Can delete log entry', 1, 'delete_logentry'); args=(u'Can add log entry', 1, u'add_logentry', u'Can change log entry', 1, u'change_logentry', u'Can delete log entry', 1, u'delete_logentry')
[vagrant@127.0.0.1:2222] out: (0.001) SELECT "django_content_type"."id", "django_content_type"."name", "django_content_type"."app_label", "django_content_type"."model" FROM "django_content_type" WHERE "django_content_type"."app_label" = 'admin'  ORDER BY "django_content_type"."name" ASC; args=('admin',)
[vagrant@127.0.0.1:2222] out: (0.000) SELECT "django_content_type"."id", "django_content_type"."name", "django_content_type"."app_label", "django_content_type"."model" FROM "django_content_type" WHERE ("django_content_type"."model" = 'permission'  AND "django_content_type"."app_label" = 'auth' ); args=('permission', 'auth')
[vagrant@127.0.0.1:2222] out: (0.000) SAVEPOINT s139976396412672_x1; args=()
[vagrant@127.0.0.1:2222] out: (0.001) INSERT INTO "django_content_type" ("name", "app_label", "model") VALUES ('permission', 'auth', 'permission') RETURNING "django_content_type"."id"; args=(u'permission', 'auth', 'permission')
[vagrant@127.0.0.1:2222] out: (0.001) SELECT "django_content_type"."id", "django_content_type"."name", "django_content_type"."app_label", "django_content_type"."model" FROM "django_content_type" WHERE ("django_content_type"."model" = 'group'  AND "django_content_type"."app_label" = 'auth' ); args=('group', 'auth')
[vagrant@127.0.0.1:2222] out: (0.000) SAVEPOINT s139976396412672_x1; args=()
[vagrant@127.0.0.1:2222] out: (0.001) INSERT INTO "django_content_type" ("name", "app_label", "model") VALUES ('group', 'auth', 'group') RETURNING "django_content_type"."id"; args=(u'group', 'auth', 'group')
[vagrant@127.0.0.1:2222] out: (0.001) SELECT "django_content_type"."id", "django_content_type"."name", "django_content_type"."app_label", "django_content_type"."model" FROM "django_content_type" WHERE ("django_content_type"."model" = 'user'  AND "django_content_type"."app_label" = 'auth' ); args=('user', 'auth')
[vagrant@127.0.0.1:2222] out: (0.000) SAVEPOINT s139976396412672_x1; args=()
[vagrant@127.0.0.1:2222] out: (0.000) INSERT INTO "django_content_type" ("name", "app_label", "model") VALUES ('user', 'auth', 'user') RETURNING "django_content_type"."id"; args=(u'user', 'auth', 'user')
[vagrant@127.0.0.1:2222] out: (0.001) SELECT "auth_permission"."content_type_id", "auth_permission"."codename" FROM "auth_permission" INNER JOIN "django_content_type" ON ("auth_permission"."content_type_id" = "django_content_type"."id") WHERE "auth_permission"."content_type_id" IN (2, 3, 4) ORDER BY "django_content_type"."app_label" ASC, "django_content_type"."model" ASC, "auth_permission"."codename" ASC; args=(2, 3, 4)
[vagrant@127.0.0.1:2222] out: (0.002) INSERT INTO "auth_permission" ("name", "content_type_id", "codename") VALUES ('Can add permission', 2, 'add_permission'), ('Can change permission', 2, 'change_permission'), ('Can delete permission', 2, 'delete_permission'), ('Can add group', 3, 'add_group'), ('Can change group', 3, 'change_group'), ('Can delete group', 3, 'delete_group'), ('Can add user', 4, 'add_user'), ('Can change user', 4, 'change_user'), ('Can delete user', 4, 'delete_user'); args=(u'Can add permission', 2, u'add_permission', u'Can change permission', 2, u'change_permission', u'Can delete permission', 2, u'delete_permission', u'Can add group', 3, u'add_group', u'Can change group', 3, u'change_group', u'Can delete group', 3, u'delete_group', u'Can add user', 4, u'add_user', u'Can change user', 4, u'change_user', u'Can delete user', 4, u'delete_user')
[vagrant@127.0.0.1:2222] out: 
[vagrant@127.0.0.1:2222] out: You just installed Django's auth system, which means you don't have any superusers defined.
[vagrant@127.0.0.1:2222] out: Would you like to create one now? (yes/no): yes
[vagrant@127.0.0.1:2222] out: (0.001) SELECT "auth_user"."id", "auth_user"."username", "auth_user"."first_name", "auth_user"."last_name", "auth_user"."email", "auth_user"."password", "auth_user"."is_staff", "auth_user"."is_active", "auth_user"."is_superuser", "auth_user"."last_login", "auth_user"."date_joined" FROM "auth_user" WHERE "auth_user"."username" = 'vagrant' ; args=('vagrant',)
[vagrant@127.0.0.1:2222] out: Username (leave blank to use 'vagrant'): admin
[vagrant@127.0.0.1:2222] out: (0.001) SELECT "auth_user"."id", "auth_user"."username", "auth_user"."first_name", "auth_user"."last_name", "auth_user"."email", "auth_user"."password", "auth_user"."is_staff", "auth_user"."is_active", "auth_user"."is_superuser", "auth_user"."last_login", "auth_user"."date_joined" FROM "auth_user" WHERE "auth_user"."username" = 'admin' ; args=('admin',)
[vagrant@127.0.0.1:2222] out: E-mail address: joshua_t@madeinhaus.com
[vagrant@127.0.0.1:2222] out: Password: 
[vagrant@127.0.0.1:2222] out: Password (again): 
[vagrant@127.0.0.1:2222] out: (0.001) INSERT INTO "auth_user" ("username", "first_name", "last_name", "email", "password", "is_staff", "is_active", "is_superuser", "last_login", "date_joined") VALUES ('admin', '', '', 'joshua_t@madeinhaus.com', 'pbkdf2_sha256$10000$qpHgJ2iqX7ST$luoNzx+6fwcX2NoS/KvysQyeT5f8PWaW763ewhXTdNE=', false, true, false, '2012-11-13 07:08:15.067973+00:00', '2012-11-13 07:08:15.067973+00:00') RETURNING "auth_user"."id"; args=('admin', '', '', 'joshua_t@madeinhaus.com', 'pbkdf2_sha256$10000$qpHgJ2iqX7ST$luoNzx+6fwcX2NoS/KvysQyeT5f8PWaW763ewhXTdNE=', False, True, False, u'2012-11-13 07:08:15.067973+00:00', u'2012-11-13 07:08:15.067973+00:00')
[vagrant@127.0.0.1:2222] out: (0.001) SELECT (1) AS "a" FROM "auth_user" WHERE "auth_user"."id" = 1  LIMIT 1; args=(1,)
[vagrant@127.0.0.1:2222] out: (0.001) UPDATE "auth_user" SET "username" = 'admin', "first_name" = '', "last_name" = '', "email" = 'joshua_t@madeinhaus.com', "password" = 'pbkdf2_sha256$10000$qpHgJ2iqX7ST$luoNzx+6fwcX2NoS/KvysQyeT5f8PWaW763ewhXTdNE=', "is_staff" = true, "is_active" = true, "is_superuser" = true, "last_login" = '2012-11-13 07:08:15.067973+00:00', "date_joined" = '2012-11-13 07:08:15.067973+00:00' WHERE "auth_user"."id" = 1 ; args=('admin', '', '', 'joshua_t@madeinhaus.com', 'pbkdf2_sha256$10000$qpHgJ2iqX7ST$luoNzx+6fwcX2NoS/KvysQyeT5f8PWaW763ewhXTdNE=', True, True, True, u'2012-11-13 07:08:15.067973+00:00', u'2012-11-13 07:08:15.067973+00:00', 1)
[vagrant@127.0.0.1:2222] out: Superuser created successfully.
[vagrant@127.0.0.1:2222] out: (0.001) SELECT "django_content_type"."id", "django_content_type"."name", "django_content_type"."app_label", "django_content_type"."model" FROM "django_content_type" WHERE "django_content_type"."app_label" = 'auth'  ORDER BY "django_content_type"."name" ASC; args=('auth',)
[vagrant@127.0.0.1:2222] out: (0.000) SELECT "django_content_type"."id", "django_content_type"."name", "django_content_type"."app_label", "django_content_type"."model" FROM "django_content_type" WHERE ("django_content_type"."model" = 'contenttype'  AND "django_content_type"."app_label" = 'contenttypes' ); args=('contenttype', 'contenttypes')
[vagrant@127.0.0.1:2222] out: (0.000) SAVEPOINT s139976396412672_x1; args=()
[vagrant@127.0.0.1:2222] out: (0.000) INSERT INTO "django_content_type" ("name", "app_label", "model") VALUES ('content type', 'contenttypes', 'contenttype') RETURNING "django_content_type"."id"; args=(u'content type', 'contenttypes', 'contenttype')
[vagrant@127.0.0.1:2222] out: (0.001) SELECT "auth_permission"."content_type_id", "auth_permission"."codename" FROM "auth_permission" INNER JOIN "django_content_type" ON ("auth_permission"."content_type_id" = "django_content_type"."id") WHERE "auth_permission"."content_type_id" IN (5) ORDER BY "django_content_type"."app_label" ASC, "django_content_type"."model" ASC, "auth_permission"."codename" ASC; args=(5,)
[vagrant@127.0.0.1:2222] out: (0.000) INSERT INTO "auth_permission" ("name", "content_type_id", "codename") VALUES ('Can add content type', 5, 'add_contenttype'), ('Can change content type', 5, 'change_contenttype'), ('Can delete content type', 5, 'delete_contenttype'); args=(u'Can add content type', 5, u'add_contenttype', u'Can change content type', 5, u'change_contenttype', u'Can delete content type', 5, u'delete_contenttype')
[vagrant@127.0.0.1:2222] out: (0.000) SELECT "django_content_type"."id", "django_content_type"."name", "django_content_type"."app_label", "django_content_type"."model" FROM "django_content_type" WHERE "django_content_type"."app_label" = 'contenttypes'  ORDER BY "django_content_type"."name" ASC; args=('contenttypes',)
[vagrant@127.0.0.1:2222] out: (0.000) SELECT "django_content_type"."id", "django_content_type"."name", "django_content_type"."app_label", "django_content_type"."model" FROM "django_content_type" WHERE ("django_content_type"."model" = 'session'  AND "django_content_type"."app_label" = 'sessions' ); args=('session', 'sessions')
[vagrant@127.0.0.1:2222] out: (0.000) SAVEPOINT s139976396412672_x1; args=()
[vagrant@127.0.0.1:2222] out: (0.000) INSERT INTO "django_content_type" ("name", "app_label", "model") VALUES ('session', 'sessions', 'session') RETURNING "django_content_type"."id"; args=(u'session', 'sessions', 'session')
[vagrant@127.0.0.1:2222] out: (0.001) SELECT "auth_permission"."content_type_id", "auth_permission"."codename" FROM "auth_permission" INNER JOIN "django_content_type" ON ("auth_permission"."content_type_id" = "django_content_type"."id") WHERE "auth_permission"."content_type_id" IN (6) ORDER BY "django_content_type"."app_label" ASC, "django_content_type"."model" ASC, "auth_permission"."codename" ASC; args=(6,)
[vagrant@127.0.0.1:2222] out: (0.000) INSERT INTO "auth_permission" ("name", "content_type_id", "codename") VALUES ('Can add session', 6, 'add_session'), ('Can change session', 6, 'change_session'), ('Can delete session', 6, 'delete_session'); args=(u'Can add session', 6, u'add_session', u'Can change session', 6, u'change_session', u'Can delete session', 6, u'delete_session')
[vagrant@127.0.0.1:2222] out: (0.000) SELECT "django_content_type"."id", "django_content_type"."name", "django_content_type"."app_label", "django_content_type"."model" FROM "django_content_type" WHERE "django_content_type"."app_label" = 'sessions'  ORDER BY "django_content_type"."name" ASC; args=('sessions',)
[vagrant@127.0.0.1:2222] out: (0.000) SELECT "django_content_type"."id", "django_content_type"."name", "django_content_type"."app_label", "django_content_type"."model" FROM "django_content_type" WHERE ("django_content_type"."model" = 'apiaccess'  AND "django_content_type"."app_label" = 'tastypie' ); args=('apiaccess', 'tastypie')
[vagrant@127.0.0.1:2222] out: (0.000) SAVEPOINT s139976396412672_x1; args=()
[vagrant@127.0.0.1:2222] out: (0.000) INSERT INTO "django_content_type" ("name", "app_label", "model") VALUES ('api access', 'tastypie', 'apiaccess') RETURNING "django_content_type"."id"; args=(u'api access', 'tastypie', 'apiaccess')
[vagrant@127.0.0.1:2222] out: (0.000) SELECT "django_content_type"."id", "django_content_type"."name", "django_content_type"."app_label", "django_content_type"."model" FROM "django_content_type" WHERE ("django_content_type"."model" = 'apikey'  AND "django_content_type"."app_label" = 'tastypie' ); args=('apikey', 'tastypie')
[vagrant@127.0.0.1:2222] out: (0.000) SAVEPOINT s139976396412672_x1; args=()
[vagrant@127.0.0.1:2222] out: (0.000) INSERT INTO "django_content_type" ("name", "app_label", "model") VALUES ('api key', 'tastypie', 'apikey') RETURNING "django_content_type"."id"; args=(u'api key', 'tastypie', 'apikey')
[vagrant@127.0.0.1:2222] out: (0.001) SELECT "auth_permission"."content_type_id", "auth_permission"."codename" FROM "auth_permission" INNER JOIN "django_content_type" ON ("auth_permission"."content_type_id" = "django_content_type"."id") WHERE "auth_permission"."content_type_id" IN (8, 7) ORDER BY "django_content_type"."app_label" ASC, "django_content_type"."model" ASC, "auth_permission"."codename" ASC; args=(8, 7)
[vagrant@127.0.0.1:2222] out: (0.000) INSERT INTO "auth_permission" ("name", "content_type_id", "codename") VALUES ('Can add api access', 7, 'add_apiaccess'), ('Can change api access', 7, 'change_apiaccess'), ('Can delete api access', 7, 'delete_apiaccess'), ('Can add api key', 8, 'add_apikey'), ('Can change api key', 8, 'change_apikey'), ('Can delete api key', 8, 'delete_apikey'); args=(u'Can add api access', 7, u'add_apiaccess', u'Can change api access', 7, u'change_apiaccess', u'Can delete api access', 7, u'delete_apiaccess', u'Can add api key', 8, u'add_apikey', u'Can change api key', 8, u'change_apikey', u'Can delete api key', 8, u'delete_apikey')
[vagrant@127.0.0.1:2222] out: (0.001) SELECT "django_content_type"."id", "django_content_type"."name", "django_content_type"."app_label", "django_content_type"."model" FROM "django_content_type" WHERE "django_content_type"."app_label" = 'tastypie'  ORDER BY "django_content_type"."name" ASC; args=('tastypie',)
[vagrant@127.0.0.1:2222] out: Installing custom SQL ...
[vagrant@127.0.0.1:2222] out: Installing indexes ...
[vagrant@127.0.0.1:2222] out: (0.002) CREATE INDEX "django_admin_log_user_id" ON "django_admin_log" ("user_id");; args=()
[vagrant@127.0.0.1:2222] out: (0.001) CREATE INDEX "django_admin_log_content_type_id" ON "django_admin_log" ("content_type_id");; args=()
[vagrant@127.0.0.1:2222] out: (0.002) CREATE INDEX "auth_permission_content_type_id" ON "auth_permission" ("content_type_id");; args=()
[vagrant@127.0.0.1:2222] out: (0.002) CREATE INDEX "auth_group_permissions_group_id" ON "auth_group_permissions" ("group_id");; args=()
[vagrant@127.0.0.1:2222] out: (0.001) CREATE INDEX "auth_group_permissions_permission_id" ON "auth_group_permissions" ("permission_id");; args=()
[vagrant@127.0.0.1:2222] out: (0.001) CREATE INDEX "auth_user_user_permissions_user_id" ON "auth_user_user_permissions" ("user_id");; args=()
[vagrant@127.0.0.1:2222] out: (0.002) CREATE INDEX "auth_user_user_permissions_permission_id" ON "auth_user_user_permissions" ("permission_id");; args=()
[vagrant@127.0.0.1:2222] out: (0.002) CREATE INDEX "auth_user_groups_user_id" ON "auth_user_groups" ("user_id");; args=()
[vagrant@127.0.0.1:2222] out: (0.001) CREATE INDEX "auth_user_groups_group_id" ON "auth_user_groups" ("group_id");; args=()
[vagrant@127.0.0.1:2222] out: (0.002) CREATE INDEX "django_session_expire_date" ON "django_session" ("expire_date");; args=()
[vagrant@127.0.0.1:2222] out: (0.000) SET CONSTRAINTS ALL IMMEDIATE; args=()
[vagrant@127.0.0.1:2222] out: (0.000) SET CONSTRAINTS ALL DEFERRED; args=()
[vagrant@127.0.0.1:2222] out: Installed 0 object(s) from 0 fixture(s)
[vagrant@127.0.0.1:2222] out: 


Done.
Disconnecting from vagrant@127.0.0.1:2222... done.
(django-template)[joshua@StigmergicProductions:~/work/haus/t/BestProject (master)]
$ fab runserver &
[1] 70302
(django-template)[joshua@StigmergicProductions:~/work/haus/t/BestProject (master)]
$ [vagrant@127.0.0.1:2222] Executing task 'runserver'
[vagrant@127.0.0.1:2222] run: ps ax | grep [p]ython | awk '{ print $1 }' | xargs kill -9


[1]+  Stopped                 fab runserver
(django-template)[joshua@StigmergicProductions:~/work/haus/t/BestProject (master)]
$ 
(django-template)[joshua@StigmergicProductions:~/work/haus/t/BestProject (master)]
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
(django-template)[joshua@StigmergicProductions:~/work/haus/t/BestProject (master)]
$ bg
[2]+ fab runserver &
(django-template)[joshua@StigmergicProductions:~/work/haus/t/BestProject (master)]
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