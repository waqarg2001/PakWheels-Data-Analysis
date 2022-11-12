from src.data.make_dataset import PakWheelsETL
import click
import logging

logger=logging.getLogger('Sales ETL')


@click.command()
@click.argument('input_filepath', type=click.Path(exists=True))
def start_etl(input_filepath):
    """
    This function starts ETL process.

    :param input_filepath: directory path where source files exist, passed as argument in terminal.
    :return: none
    """
    etl = PakWheelsETL()
    etl.ETL(input_filepath)
    logger.info('ETL process terminated.')


if __name__ == '__main__':

    start_etl()

