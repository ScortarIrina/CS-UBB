;;a) union of two sets

(defun contains (l x)
    (cond 
        ((null l) 0)
        ((eq (car l) x) 1)
        (t (contains (cdr l) x))
    )
)

(defun unionRec (l v)
    (cond 
        ((null l) v)
        ((= (contains v (car l)) 0) (unionRec (cdr l) (append v (list (car l)))))
        (t (unionRec (cdr l) v))
    )
)

(defun union2 (a b)
    (unionRec b a)
)

(print (union2 '(1 2 3) '(1 2 3 4)))
