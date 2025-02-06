from loguru import logger

logger.debug("Um aviso para o desenvolver no futuro, enquanto debuga")
logger.info("Informação importante para ser mostrada durante o processo/execução")
logger.warning("Um aviso que algo vai falhar ou parar de funcionar no futuro")
logger.error("Aconteceu uma falha")
logger.critical("Aconteceu uma falha que aborta a aplicação")