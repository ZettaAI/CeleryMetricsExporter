import click
from typing import List
from src.exporter import CeleryMetricsExporter

@click.command(context_settings={"auto_envvar_prefix": "CELERY_EXPORTER"})

@click.option(
    "--broker-url", required=True, help="The url to the broker, e.g redis://1.2.3.4"
)
@click.option(
    "--port",
    type=int,
    default=9540,
    show_default=True,
    help="The port the exporter will listen on",
)
@click.option(
    "-q",
    "--queue-names",
    multiple=True,
    required=True,
    help="The queues to track",
)
@click.option(
    "-r",
    "--refresh",
    type=int,
    default=30,
    show_default=True,
    help="How often to refresh metrics in seconds",
)


def cli(broker_url: str, port: int, queue_names: List[str]):
    ctx = click.get_current_context()
    params = ctx.params
    broker_url = params["broker_url"]
    port = params["port"]
    queue_names = params["queue_names"]
    metrics_refresh = params["refresh"]
    exporter = CeleryMetricsExporter(broker_url, queue_names, port, metrics_refresh)
    exporter.run()


