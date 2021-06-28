%global debug_package %{nil}

Name: corteza
Version: %{_rpm_version}
Release: %{_rpm_release}
Summary: Corteza

Group: Applications/Productivity
License: ASL 2.0
URL: https://cortezaproject.org
Source0: corteza-%{_version}-linux-amd64.tar.gz

AutoReqProv: no

Requires: systemd


%description
Corteza brings your user ecosystem and essential applications together on one platform, unifying them via CRM, Advanced Identity and Access Management.

Corteza CRM Corteza CRM is the highly flexible, scalable and open source Salesforce alternative, that enables your team to sell faster. It provides a 360 degree view of your customers, enabling you to service your prospects better and detect new opportunities.

Corteza Low Code Corteza Low Code is the flexible and easy to use open source Low Code Development platform for custom web based business applications, with drag and drop builder features, integrated Identity, Access and Privacy Management, and powerful automation options. Corteza CRM is based on Low Code.

Corteza One Corteza One manages the user experience for Corteza applications, such as CRM, and Low Code, as well as providing an integrated interface for third party or other bespoke applications. 100% responsive and with an intuitive design, Corteza One increases productivity and ease of access to all IT resources.

%prep
%setup -c -n corteza


%build


%install
mkdir -p $RPM_BUILD_ROOT/var/corteza
mkdir -p $RPM_BUILD_ROOT/lib/systemd/system
mkdir -p $RPM_BUILD_ROOT/opt
mkdir -p $RPM_BUILD_ROOT/etc


cp -a $RPM_BUILD_DIR/corteza $RPM_BUILD_ROOT/opt/corteza


cat > $RPM_BUILD_ROOT/etc/corteza-server.conf << EOL
# Corteza configuration

# Note: default docker image without any extra command will
# force :80 via flag and override anything you set here
HTTP_ADDR=:80

HTTP_WEBAPP_ENABLED=true
HTTP_WEBAPP_BASE_DIR=/opt/corteza/webapp

DOMAIN=localhost

# Database to use
#DB_DSN=corteza:corteza@tcp(localhost:3306)/corteza?collation=utf8mb4_general_ci

# Logging level we want to use (values: debug, info, warn, error, dpanic, panic, fatal)
LOG_LEVEL=info

# Enable debug logger (more verbose,
#LOG_DEBUG=false

########################################################################################################################
# Storage configuration

# Local, plain storage path:

STORAGE_PATH=/var/corteza

EOL


cat > $RPM_BUILD_ROOT/lib/systemd/system/corteza-server.service << EOL
[Unit]
Description=Corteza Server Service

[Service]
WorkingDirectory=/opt/corteza/bin
ExecStart=/opt/corteza/bin/corteza-server serve-api

[Install]
WantedBy=multi-user.target

EOL


%files
/opt/corteza
/var/corteza
/lib/systemd/system/corteza-server.service
/etc/corteza-server.conf


%post
ln -s /etc/corteza-server.conf /opt/corteza/bin/.env


%postun
rm -rf /opt/corteza/bin/.env


%changelog
