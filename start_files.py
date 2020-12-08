import test, testexport
import multiprocessing

for file in ('testexport', 'test'):
	p=multiprocessing.Process(target=lambda: _import_(file))
	p.start()