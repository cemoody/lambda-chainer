# lambda-chainer
AWS Lambda function with Numpy, protobuf, pillow, and Chainer

Followed the steps outlined [here](https://serverlesscode.com/post/deploy-scikitlearn-on-lamba/)
 but added more common scientific python libraries.

The total zipped size comes to 22MB, leaving some wiggle room for extra libraries.

Instructions:

	sudo yum -y upgrade
	sudo yum -y groupinstall "Development Tools"
	sudo yum -y install blas blas-devel lapack \
	     lapack-devel Cython --enablerepo=epel


	pip install virtualenv
	virtualenv ~/env && cd ~/env && source bin/activate
	pip install numpy
	pip install Pillow
	pip install --use-wheel --no-index -f http://dist.plone.org/thirdparty/ -U PIL
	pip install protobuf
	cd
	touch env/lib/python2.7/site-packages/google/__init__.py
	pip install chainer

	for dir in $VIRTUAL_ENV/lib64/python2.7/site-packages \
		   $VIRTUAL_ENV/lib/python2.7/site-packages
	do
	  if [ -d $dir ] ; then
	    pushd $dir; zip -9 -q -r ~/deps.zip .; popd
	  fi
	done

	cd
	git clone https://github.com/google/protobuf.git
	cd protobuf
	zip -9 -q -r ~/deps.zip python

	cd; cd lambda-chainer; zip -9 -q -r ~/deps.zip test.py; cd


	cd
	mkdir -p local/lib
	cp /usr/lib64/liblapack.so.3 \
	   /usr/lib64/libblas.so.3 \
	   /usr/lib64/libgfortran.so.3 \
	   /usr/lib64/libquadmath.so.0 \
	   local/lib/
	zip -r ~/deps.zip local/lib

