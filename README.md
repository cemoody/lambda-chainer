# lambda-chainer
AWS Lambda function with Numpy, protobuf, pillow, and Chainer

Followed the steps outlined [here](https://serverlesscode.com/post/deploy-scikitlearn-on-lamba/)
 but added more common scientific python libraries.

The total zipped size comes to 22MB, leaving some wiggle room for extra libraries.

Instructions:

	sudo yum install -y atlas-devel atlas-sse3-devel blas-devel gcc gcc-c++ lapack-devel python27-devel

	/usr/bin/virtualenv \
	      --python /usr/bin/python chainer_build \
	      --always-copy \
	       --no-site-packages
	source chainer_build/bin/activate
	pip install --use-wheel numpy
	pip install --use-wheel chainer
	pip install --use-wheel --no-index -f http://dist.plone.org/thirdparty/ -U PIL
	# pip install --use-wheel scipy
	# pip install --use-wheel sklearn
	# pip install --use-wheel cython
	# pip install --use-wheel pandas


	git clone https://github.com/google/protobuf.git
	cd protobuf/python 
	(cd .. && make)
	export LD_LIBRARY_PATH=../src/.libs
	python setup.py build 



	source chainer_build/bin/activate
	find "$VIRTUAL_ENV/lib64/python2.7/site-packages/" -name "*.so" | xargs strip
	# This fixes the stupid protobuf problem
	touch chainer_build/lib/python2.7/site-packages/google/__init__.py
	rm -rdf venv.zip
	cd $VIRTUAL_ENV/lib64/python2.7/site-packages/
	zip -r -9 -q ~/venv.zip * 
	cd $VIRTUAL_ENV/lib/python2.7/site-packages/
	zip -r -9 -q ~/venv.zip *
	cd $VIRTUAL_ENV/src/protobuf
	zip -r -9 -q ~/venv.zip python
	cd ~/lambda-chainer
	zip -r -9 -q ~/venv.zip test.py
	cd
	cd /usr/lib64/atlas
	zip -r -9 -q ~/venv.zip *
	cd

	ls -alh *zip



	cd; cp lambda-chainer/test.py .
	cd; rm -rdf temp; mkdir temp; cp venv.zip temp/; cd temp/; unzip venv.zip; python test.py
