# Corteza

Repository to unify *Corteza Server* and *Corteza Webapp*:

* [corteza-server](https://github.com//cortezaproject/corteza-server)
* [corteza-webapp](https://github.com//cortezaproject/corteza-webapp)

## GitHub Actions

### Release

In order to do release you need to tag all composed *webapp* repositories.
Once you tag main branch, the [pipeline](https://github.com/cortezaproject/corteza/blob/main/.github/workflows/release.yml) is being executed.

We are currently releasing:

* Compressed artifacts stored in [https://releases.cortezaproject.org/files](https://releases.cortezaproject.org/files)
* Docker image stored in [https://hub.docker.com/r/cortezaproject/corteza](https://hub.docker.com/r/cortezaproject/corteza)
* RPM package stored in [https://releases.cortezaproject.org/files](https://releases.cortezaproject.org/files)

#### RPM package requirements

RPM packages has being tested on Red Hat Linux Enterprise 8. 

In order to install Corteza rpm package you need first need to install

* [musl-filesystem-1.2.1-1.el8.x86_64.rpm](https://releases.cortezaproject.org/files/musl-filesystem-1.2.1-1.el8.x86_64.rpm)
* [musl-libc-1.2.1-1.el8.x86_64.rpm](https://releases.cortezaproject.org/files/musl-libc-1.2.1-1.el8.x86_64.rpm)

```
wget https://releases.cortezaproject.org/files/musl-filesystem-1.2.1-1.el8.x86_64.rpm
wget https://releases.cortezaproject.org/files/musl-libc-1.2.1-1.el8.x86_64.rpm
rpm -i musl-filesystem-1.2.1-1.el8.x86_64.rpm musl-libc-1.2.1-1.el8.x86_64.rpm
```