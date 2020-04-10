# Folding @ Home SELinux Policy

This repo contains an SELinux policy for the Folding @ Home client
on Red Hat Enterprise Linux and similar systems that use SELinux like CentOS

## Building the policy module

### Dependencies

 - policycoreutils-devel
 - rpm-build
 - make

```
   yum install policycoreutils-devel rpm-build make
```

 Build the policy module

```
./fah.sh
```

## Installing the policy module

