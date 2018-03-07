{-
Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees. Can you do this in place?

This solution is not in place nor is it efficient (the reversal operation is an O(N) operation, (!!) is also O(N), etc), but...elegant. Thx Haskell
-}

main  = print $ show $ rotate [[1,2,3],[4,5,6],[7,8,9]] 3

-- rotate an NxN matrix. Must specify dimension N
rotate :: [[a]] -> Int -> [[a]]
rotate mat n = map getReversedRow [0..n-1]
  where reversed = reverse mat
        getReversedRow = \i -> map (flip (!!) i) reversed
