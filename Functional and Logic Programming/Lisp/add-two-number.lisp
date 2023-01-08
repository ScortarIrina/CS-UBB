;; This buffer is for text that is not saved, and for Lisp evaluation.
;; To create a file, visit it with C-x C-f and enter text in its buffer.

(defun add-two-number (n1 n2)
  "Adds two numbers"
  (+ n1 n2)
)
(write(add-two-number 10 20))
