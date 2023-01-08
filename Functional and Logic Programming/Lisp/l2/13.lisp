; Define a function that returns the depth of a tree represented as (root list_of_nodes_subtree1 ... list_of_nodes_subtreen)
;     Eg. the depth of the tree (a (b (c)) (d) (e (f))) is 3


; my_max(a, b) = { nil, if a is not a number and b is not a number
;              = { a, if b is not a number
;              = { b, if a is not a number
;              = { a, if a > b
;              = { b, otherwise
; function to retriele the maximum between 2 elements
(defun my_max(a b)
  (cond
    ((and (not (numberp a)) (not (numberp b))) nil)
    ((not (numberp b)) a)
    ((not (numberp a)) b)
    ((> a b) a)
    (t b)
  )
)


; find_max(l1 l2 ... ln) = { nil, if n = 0
;                        = { my_max(l1, find_max(l2 ... ln)), otherwise
; function to retrieve the maximum element in a list
(defun find_max(l)
  (cond
    ((null l) nil)
    (t (my_max (car l) (find_max (cdr l))))
  )
)


; find_depth_tree(tree, counter) = { counter, if tree is an atom
;                                = { find_max(find_depth_tree(tree1, counter + 1), find_depth_tree(tree2, counter + 1), ... , find_depth_tree(treen, counter + 1)), otherwise
; function to compute the depth of a tree
(defun find_depth_tree(tree counter)
  (cond
    ((atom tree) counter)     ; we stop the recursion when the tree consists of one atom
    (t (apply #'find_max (list (mapcar #' (lambda (a) (find_depth_tree a (+ 1 counter))) tree))))
  )
)

(defun main(l)
  (find_depth_tree l 0)
)



(defun test_main ()
    (assert
	    (and
	        (equal 3 (main '(A (B (C)) (D) (E (F)))))
            (equal 5 (main '(A (B) (C (D) (E (F) (G (H) (I J K)))))))
	    )
    )
)


;     FIRST TEST                           SECOND TEST
;
;         A                                     A
;        / \                                   / \
;       /   \                                 /   \
;      B     D                               B     C
;     /     /                                     / \
;    /     /                                     /   \
;   C     E                                     D     E
;        /                                           / \
;       /                                           /   \
;      F                                           F     G
;                                                       / \
;                                                      /   \
;                                                     H     I
;                                                          / \  
;                                                         /   \
;                                                        J     K




; (compile-file "/Users/irinascortar/Desktop/VSCode_projects/LISP/l2/13.lisp")
; (load "/Users/irinascortar/Desktop/VSCode_projects/LISP/l2/13.lisp")