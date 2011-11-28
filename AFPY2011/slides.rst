================================================================================
Segmentation d'images
================================================================================

-----

La segmentation d'image
--------------------------------------------------------------------------------

  "La **segmentation d'image** est une opération de **traitement d'images**
  qui a pour but de **rassembler** des pixels entre eux suivant des **critères
  pré-définis**" -- *wikipedia*




.. image:: code/segments_3.png
  :scale: 40 %

---------

L'Apprentissage Statistique
--------------------------------------------------------------------------------

  "L'apprentissage automatique (machine learning en anglais), un des champs
  d'étude de **l'intelligence artificielle**, est la discipline scientifique
  concernée par **le développement, l'analyse et l'implémentation de méthodes
  automatisables** qui permettent à une machine (au sens large) **d'évoluer
  grâce à un processus d'apprentissage,** et ainsi de remplir des tâches qu'il
  est difficile ou impossible de remplir par des moyens algorithmiques plus
  classiques." -- **wikipedia**

.. raw:: html

  <span class="regression">

.. image:: images/regression_linear.png
  :scale: 85%

.. raw:: html

  </span>


-----


L'Apprentissage Supervisé
--------------------------------------------------------------------------------

ou analyse discriminante
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Production automatique de règles à partir d'une base de données contenant
  des cas déjà traités et validés

  - **Classification**
  - **Regression**

.. raw:: html

  <span class="hyperplan">

.. image:: images/hyperplane.png
  :scale: 90%

.. raw:: html

  </span>


--------------------------------------------------------------------------------


L'Apprentissage Non Supervisé
--------------------------------------------------------------------------------

ou classification automatique
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


- Division d'un groupe de données en sous groupes de données similaires


.. image:: images/ward.png

----

Scikit-Learn
--------------------------------------------------------------------------------

L'apprentissage statistique en python
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: code/sklearn_2.png
  :scale: 25 %

-----

L'algorithme - Etape 0
--------------------------------------------------------------------------------

.. image:: code/figure_0.png

----

L'algorithme - Etape 1
--------------------------------------------------------------------------------

.. image:: code/figure_1.png


----

L'algorithme - Etape 2
--------------------------------------------------------------------------------

.. image:: code/figure_2.png

----

L'algorithme - Etape 3
--------------------------------------------------------------------------------

.. image:: code/figure_3.png

----

L'algorithme
--------------------------------------------------------------------------------

.. image:: code/figure_10.png


----

Application sur une image
--------------------------------------------------------------------------------

- Cohérence spatiale
- Cohérence de couleur

.. image:: code/couleurs_3d.png
  :scale: 75 %

----

Image initiale: Baboon
--------------------------------------------------------------------------------

.. image:: code/baboon.jpg

----

Exemple - gris
--------------------------------------------------------------------------------

.. image:: code/baboon_gris_8.png

----

Exemple - Couleurs
--------------------------------------------------------------------------------

.. image:: code/baboon_couleur_30.png

----

Question ?

.. image:: code/python_seg_1.png
    :scale: 50 %
