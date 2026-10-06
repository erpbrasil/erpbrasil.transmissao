
Changelog
=========

0.0.0 (2019-09-17)
~~~~~~~~~~~~~~~~~~

* First release on PyPI.


1.0.0 (2020-11-10)
~~~~~~~~~~~~~~~~~~

* Fim do suporte ao python2
* Estabilização dos testes

1.2.0 (não publicada)
~~~~~~~~~~~~~~~~~~~~~

* Empacotamento: ``pyproject.toml`` com hatchling, namespace ``erpbrasil`` por
  ``pkgutil.extend_path`` (igual à ``erpbrasil.base``), extras ``test`` e ``doc``,
  Python 3.6 a 3.14 declarado e testado no CI (o Travis estava morto desde 2020),
  publicação no PyPI por Release do GitHub com conferência da tag.
* ``erpbrasil.monkey_patch`` passa a viver em ``erpbrasil.transmissao.monkey_patch``
  (deixa de ocupar um pacote próprio no namespace compartilhado).
* Suíte de testes volta a rodar: os testes não executam mais na importação do
  módulo, o certificado de teste expirado é aceito e os caminhos dos cassetes são
  relativos ao arquivo de teste.
