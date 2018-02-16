main = do
  mapM_ (putStrLn . show) findAllQueenPositions

data Position = Position {
                          rowIndex :: Int,
                          colIndex :: Int
                         }

instance Show Position where
  show (Position row col) = "(" ++ (show row) ++ ", " ++ (show col) ++ ")"


findAllQueenPositions ::  [[Position]]
findAllQueenPositions = findPositions 8 []

findPositions :: Int -> [Position] -> [[Position]]
findPositions 0 currPositions          = [currPositions]
findPositions queensLeft currPositions = concatMap (findPositionsIfValid (queensLeft - 1) currPositions) newPositions
  where newPositions = [Position currRow currCol | currCol <- [0..7]]
        currRow      = length currPositions
        findPositionsIfValid = \qLeft currPos newPos-> if isValidLayout currPos newPos
                                                          then findPositions qLeft (newPos : currPos)
                                                          else []



isValidLayout :: [Position] -> Position -> Bool
isValidLayout []  _ = True
isValidLayout currPositions p@(Position row col) | row `elem` rowVals     = False
                                                 | col `elem` colVals       = False
                                                 | p `isInDiagAll` currPositions = False
                                                 | otherwise                = True
                                                   where rowVals = [rowIndex x | x <- currPositions]
                                                         colVals = [colIndex x | x <- currPositions]

isInDiagAll :: Position -> [Position] -> Bool
isInDiagAll newPos currPositions = any (isInDiag newPos) currPositions

isInDiag (Position rowX colX) (Position rowY colY) = abs (rowX - rowY) == abs (colX - colY)
