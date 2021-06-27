%global debug_package %{nil}

Name: corteza
Version: 2021.3.5
Release: 1
Summary: Corteza

Group: Applications/Productivity
License: ASL 2.0
URL: https://cortezaproject.org
Source0: corteza-2021.3.5-linux-amd64.tar.gz


Requires: systemd


%description
Corteza brings your user ecosystem and essential applications together on one platform, unifying them via CRM, Advanced Identity and Access Management.

Corteza CRM Corteza CRM is the highly flexible, scalable and open source Salesforce alternative, that enables your team to sell faster. It provides a 360 degree view of your customers, enabling you to service your prospects better and detect new opportunities.

Corteza Low Code Corteza Low Code is the flexible and easy to use open source Low Code Development platform for custom web based business applications, with drag and drop builder features, integrated Identity, Access and Privacy Management, and powerful automation options. Corteza CRM is based on Low Code.

Corteza One Corteza One manages the user experience for Corteza applications, such as CRM, and Low Code, as well as providing an integrated interface for third party or other bespoke applications. 100% responsive and with an intuitive design, Corteza One increases productivity and ease of access to all IT resources.

%prep
%setup -n corteza


%build


%install
mkdir -p $RPM_BUILD_ROOT/var/corteza
mkdir -p $RPM_BUILD_ROOT/%{_unitdir}
mkdir -p $RPM_BUILD_ROOT/opt


cp -a $RPM_BUILD_DIR/corteza $RPM_BUILD_ROOT/opt/corteza
mv $RPM_BUILD_ROOT/opt/corteza/bin/corteza-server $RPM_BUILD_ROOT/opt/corteza/corteza-server
rm -rf $RPM_BUILD_ROOT/opt/corteza/bin


cat > $RPM_BUILD_ROOT/opt/corteza/.env << EOL
# Corteza configuration

# Note: default docker image without any extra command will
# force :80 via flag and override anything you set here
HTTP_ADDR=:80

HTTP_WEBAPP_ENABLED=true

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


cat > $RPM_BUILD_ROOT%{_unitdir}/corteza-server.service << EOL
[Unit]
Description=Corteza Server Service

[Service]
WorkingDirectory=/opt/corteza
ExecStart=/opt/corteza/corteza-server serve-api

[Install]
WantedBy=multi-user.target

EOL



%files
/opt/corteza
/var/corteza
%{_unitdir}/corteza-server.service


%post
ln -s /opt/corteza/.env /etc/corteza-server.conf


%postun
rm -rf /etc/corteza-server.conf


%changelog
