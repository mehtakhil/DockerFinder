from pyfinder import Crawler
from pyfinder import build_test
from docopt import docopt

__doc__= """Crawler

Usage:
  Crawler.py crawl  [--amqp-url=<amqp://guest:guest@rabbitmq:5672>] [--queue=<dofinder>] [--ex=<dofinder>] [--key=<images.scan>]  [--fp=<1>] [--ps=<10>]  [--mi=<100>]
  Crawler.py pull testImages [--ni=<100>] [--pf=<images.test>]
  Crawler.py push testImages   [--amqp-url=<amqp://guest:guest@rabbitmq:5672>] [--ex=<dofinder>] [--key=<images.scan>]  [--queue=<test>]  [--pf=<images.test>]
  Crawler.py (-h | --help)
  Crawler.py --version

Options:
  -h --help     Show this screen.
  --amqp_url=AMQP_URL  Complete amqp url of the rabbitMQ server     [default: amqp://guest:guest@rabbitmq:5672]
  --queue=QUEUE        Queue is the name of the queue of rabbitMQ   [default: images]
  --ex=EXCHANGE        Exchange name in the rabbitMQ.               [default: dofinder]
  --key=KEY            Key routing for the rabbitMQ.                [default: images.scan]
  --fp=FROM_PAGE      From Page: starting page crawled from the docker hub [default: 1].
  --ps=PAGE_SIZE      number of images in a single page [default: 10].
  --mi=MAX_PAGE       Max number of images to be craw from the docker hub [default: 100].
  --ni=NUMBER_IMAGES  Number of images to crawl in order to run the test [default: 100].
  --pf=PATH_FILE      Path of the file containing the set of images to test [default: images.test]
  --version     Show version.
"""

if __name__ == '__main__':
    args = docopt(__doc__, version='Crawler 0.0.1')
    # print(args)
    if args['crawl']:
        crawler = Crawler(amqp_url=args['--amqp-url'], queue=args['--queue'], exchange=args['--ex'], route_key=args['--key'])
        crawler.run(max_images=int(args['--mi']), page_size=int(args['--ps']), from_page=int(args['--fp']))
        #crawler.crawl(max_images=int(args['--mi']), page_size=int(args['--ps']), from_page=int(args['--fp']))

    if args['pull'] and args['testImages']:
        build_test(path_name_file=args['--pf'], num_images_test=int(args['--ni']))

    if args['push'] and args['testImages']:
        crawler = Crawler(amqp_url=args['--amqp-url'], queue=args['--queue'], exchange=args['--ex'], route_key=args['--key'])
        crawler.run_test(path_name_file=args['--pf'])

