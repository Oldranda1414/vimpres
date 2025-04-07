---
marp: true
theme: gaia
paginate: true
class: invert
---

<!--
Voce ok?
seminario sarà registrato
Mi presento
Alzate le mani, interrompetemi pure
Durata seminario: 1h presentazione + 30m demo
hai detto seminario sarà registrato?
-->

<style>
section::after {
  content: attr(data-marpit-pagination) '/' attr(data-marpit-pagination-total);
}
</style>

<!-- _class: lead invert -->
<!-- _paginate: false -->

# Vim Bindings nel 2025

Leonardo Randacio

---

<!-- _class: invert lead -->

# Premessa

---

<!-- _paginate: hold -->

## Premessa

Questo seminario __non è__ un tutorial di Vim

Questo seminario è un __introduzione__ ai __Vim Bindings__

__Non dirò:__

-
-

---

<!-- _paginate: hold -->

## Premessa

Questo seminario __non è__ un tutorial di Vim

Questo seminario è un __introduzione__ ai __Vim Bindings__

__Non dirò:__

- di passare a Vim
-

---

<!-- _paginate: hold -->

## Premessa

Questo seminario __non è__ un tutorial di Vim

Questo seminario è un __introduzione__ ai __Vim Bindings__

__Non dirò:__

- di passare a Vim
- come uscire da Vim

---

## Prerequisiti

-
-

---

<!-- _paginate: hold -->

## Prerequisiti

- Pazienza
-

---

<!-- _paginate: hold -->

## Prerequisiti

- Pazienza
- Touch Typing

---

## Perché usare i Vim Bindings?

-
-
-

---

<!-- _paginate: hold -->

## Perché usare i Vim Bindings?

- Smettere di usare il __mouse__
-
-

---

<!-- _paginate: hold -->

## Perché usare i Vim Bindings?

- Smettere di usare il __mouse__
- Smettere di usare le __arrow keys__
-

---

<!-- _paginate: hold -->

## Perché usare i Vim Bindings?

- Smettere di usare il __mouse__
- Smettere di usare le __arrow keys__
- Risparmiarsi di imparare __shortcuts__ improponibili

---

<!-- _class: invert lead -->

# Vim Modes

---

## Vim Modes

![h:500px](images/vim_modes.png)

---

## Vim Modes

Abbiamo __26__ nuovi shortcut!

__52__ se usiamo \<shift\> !!!

Vedremo solo i __più utili__

---

<!-- _class: invert lead -->

# Motions

---

## Motions

Al posto delle __arrow keys__:

- ⬆️ → __k__
- ⬇️ → __j__
- ➡️ → __l__
- ⬅️ → __h__

---

<!-- _paginate: hold -->

## Motions

Al posto delle __arrow keys__:

- ⬆️&nbsp;&nbsp; →&nbsp;&nbsp; __k__
- ⬇️&nbsp;&nbsp; →&nbsp;&nbsp; __j__
- ➡️&nbsp;&nbsp; →&nbsp;&nbsp; __l__
- ⬅️&nbsp;&nbsp; →&nbsp;&nbsp; __h__

### Ehhhhhh?!

---

## Motions

![h:380](images/touch_typing.png)

---

![h:600](images/takemymoney.jpg)

---

## Motions

- __w__ (word), __b__ (back)&nbsp;&nbsp; →&nbsp;&nbsp; destra/sinistra di una parola
- __0__, __$__&nbsp;&nbsp; →&nbsp;&nbsp; inizio e fine di una riga
- __gg__, __G__&nbsp;&nbsp; →&nbsp;&nbsp; inizio e fine del file

---

<!-- _paginate: hold -->

## Motions

- __w__ (word), __b__ (back)&nbsp;&nbsp; →&nbsp;&nbsp; destra/sinistra di una parola
- __0__, __$__&nbsp;&nbsp; →&nbsp;&nbsp; inizio e fine di una riga
- __gg__, __G__&nbsp;&nbsp; →&nbsp;&nbsp; inizio e fine del file

__Anche con numeri:__

- __2j__&nbsp;&nbsp; →&nbsp;&nbsp; giù di 2 righe
- __20G__&nbsp;&nbsp; →&nbsp;&nbsp; vai a riga 20

---

<!-- _class: invert lead -->

# Operators

---

## Operators

- __x__ (cross)&nbsp;&nbsp; →&nbsp;&nbsp; elimina un carattere
- __dd__ (delete)&nbsp;&nbsp; →&nbsp;&nbsp; elimina una riga
- __yy__ (yank)&nbsp;&nbsp; →&nbsp;&nbsp; copia una riga
- __p__ (paste)&nbsp;&nbsp; →&nbsp;&nbsp; incolla
- __u__ (undo)&nbsp;&nbsp; →&nbsp;&nbsp; indietro di un azione
- __\<ctrl\> + r__ (redo)&nbsp;&nbsp; →&nbsp;&nbsp; avanti di un azione

---

## Operators

- __i__ (insert)&nbsp;&nbsp; →&nbsp;&nbsp; passa a Insert prima del cursore
- __a__ (append)&nbsp;&nbsp; →&nbsp;&nbsp; passa a Insert dopo il cursore
- __o__ (open)&nbsp;&nbsp; →&nbsp;&nbsp; new line e passa a Insert
- __cc__ (change)&nbsp;&nbsp; →&nbsp;&nbsp; elimina riga e passa a Insert
- __v/V__ (visual)&nbsp;&nbsp; →&nbsp;&nbsp; passa a character/line wise Visual
-
-

---

## Operators

<!-- _paginate: hold -->

- __i__ (insert)&nbsp;&nbsp; →&nbsp;&nbsp; passa a Insert prima del cursore
- __a__ (append)&nbsp;&nbsp; →&nbsp;&nbsp; passa a Insert dopo il cursore
- __o__ (open)&nbsp;&nbsp; →&nbsp;&nbsp; new line e passa a Insert
- __cc__ (change)&nbsp;&nbsp; →&nbsp;&nbsp; elimina riga e passa a Insert
- __v/V__ (visual)&nbsp;&nbsp; →&nbsp;&nbsp; passa a character/line wise Visual
- __I__&nbsp;&nbsp; →&nbsp;&nbsp; ???
- __A__&nbsp;&nbsp; →&nbsp;&nbsp; ???

---

## Operators

<!-- _paginate: hold -->

- __i__ (insert) &nbsp;&nbsp;→ &nbsp;&nbsp;passa a Insert prima del cursore
- __a__ (append) &nbsp;&nbsp;→ &nbsp;&nbsp;passa a Insert dopo il cursore
- __o__ (open) &nbsp;&nbsp;→ &nbsp;&nbsp;new line e passa a Insert
- __cc__ (change) &nbsp;&nbsp;→ &nbsp;&nbsp;elimina riga e passa a Insert
- __v/V__ (visual)&nbsp;&nbsp; →&nbsp;&nbsp; passa a character/line wise Visual
- __I__ &nbsp;&nbsp;→ &nbsp;&nbsp;inizio riga e passa a Insert
- __A__ &nbsp;&nbsp;→ &nbsp;&nbsp;fine riga e passa a Insert

---

<!-- _class: invert lead -->

# Vim Grammar

---

## Vim Grammar

_Mangio_ UNA __mela__

_Verbo_ + QUANTITÀ + __Sostantivo__&nbsp;&nbsp; →&nbsp;&nbsp; _Operator_ + COUNT + __Motion__

---

## Vim Grammar

_Verbo_ + QUANTITÀ + __Sostantivo__&nbsp;&nbsp; →&nbsp;&nbsp; _Operator_ + COUNT + __Motion__

- __d2w__ (delete 2 word)&nbsp;&nbsp; →&nbsp;&nbsp; elimina due parole

---

## Vim Grammar

<!-- _paginate: hold -->

_Verbo_ + QUANTITÀ + __Sostantivo__&nbsp;&nbsp; →&nbsp;&nbsp; _Operator_ + COUNT + __Motion__

- __d2w__ (delete 2 word)&nbsp;&nbsp; →&nbsp;&nbsp; elimina due parole
- __y$__ (yank line end)&nbsp;&nbsp; →&nbsp;&nbsp; copia fino a fine riga

---

## Vim Grammar

<!-- _paginate: hold -->

_Verbo_ + QUANTITÀ + __Sostantivo__&nbsp;&nbsp; →&nbsp;&nbsp; _Operator_ + COUNT + __Motion__

- __d2w__ (delete 2 word)&nbsp;&nbsp; →&nbsp;&nbsp; elimina due parole
- __y$__ (yank line end)&nbsp;&nbsp; →&nbsp;&nbsp; copia fino a fine riga
- __gU2j__ (go upper 2 down)&nbsp;&nbsp; →&nbsp;&nbsp; rendi maiuscole le prossime 3 righe

---

## Vim Grammar

<!-- _paginate: hold -->

_Verbo_ + QUANTITÀ + __Sostantivo__ → _Operator_ + COUNT + __Motion__

- __d2w__ (delete 2 word)&nbsp;&nbsp; →&nbsp;&nbsp; elimina due parole
- __y$__ (yank line end)&nbsp;&nbsp; →&nbsp;&nbsp; copia fino a fine riga
- __gU2j__ (go upper 2 down)&nbsp;&nbsp; →&nbsp;&nbsp; rendi maiuscole le prossime 3 righe
- __ci(__ (change inner parentheses)&nbsp;&nbsp; →&nbsp;&nbsp; elimina il contenuto della
  parentesi e passa a Insert

---

## Vim Grammar

Il comando più usato:

__.__ (dot)&nbsp;&nbsp; →&nbsp;&nbsp; ripeti l'ultimo comando

---

<!-- _class: invert lead -->

# Eureka!!!

---

## Eureka!!!

Proviamo a intuire comandi che non abbiamo mai visto:

```py
print("Hello World") # Questo commento è inutile.
```

---

## Eureka!!!

Proviamo a intuire comandi che non abbiamo mai visto:

Ricorda: __gU__ → rendi maiuscolo

```py
variabile_globale = 1

"""
QUESTO DOVREBBE
ESSERE
TUTTO MINUSCOLO
"""

```

---

## Come Imparare

- Armarsi di __pazienza__
- Installare __estensione__ per il proprio IDE preferito
- Imparare i comandi in maniera __incrementale__
- Chiedersi "posso fare di meglio?"

---

<!-- _class: invert lead -->
<!-- _paginate: false -->

# __Domande?__

Lucidi → https://oldranda1414.github.io/vimpres/
Autore → leonardo.randacio@studio.unibo.it

---

<!-- _class: invert lead -->
<!-- _paginate: false -->

## Pausa e poi ...

# __Demo__

---

# Estensioni

- vscode -> vim
- pycharm -> ideaVim
- jupyter -> __NON USATELO__

---

<!--
Interessa argomento?
-->
<!-- _class: invert lead -->
<!-- _paginate: false -->

# Grazie per l'attenzione

Lucidi → https://oldranda1414.github.io/vimpres/
Autore → leonardo.randacio@studio.unibo.it
