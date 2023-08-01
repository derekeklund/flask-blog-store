-- CREATE TABLE averageReviews(productID INTEGER NOT NULL PRIMARY KEY, productName TEXT NOT NULL, avgReview REAL NOT NULL);

-- CREATE TABLE userReviews (productID INTEGER NOT NULL, productName TEXT NOT NULL, reviewerName TEXT NOT NULL, reviewTitle TEXT NOT NULL, reviewBody TEXT NOT NULL, rating REAL NOT NULL, FOREIGN KEY (productID) REFERENCES averageReviews(productID));

-- INSERT INTO averageReviews(productID, productName, avgReview) VALUES (1, "Subprime_Mug", 0.0);

-- INSERT INTO averageReviews(productID, productName, avgReview) VALUES (2, "FTX_Mug", 0.0);

-- SELECT * FROM averageReviews;

SELECT * FROM userReviews;

-- SELECT avgReview FROM averageReviews WHERE productName = 'Subprime_Mug';

-- SELECT avgReview FROM averageReviews WHERE productName = 'Subprime_Mug';


-- Test code below

-- INSERT INTO averageReviews(productID, productName, avgReview) VALUES (999, "Mr_Garrison's_Penis", 0.0);

-- INSERT INTO userReviews (productID, productName, reviewerName, reviewTitle, reviewBody, rating) VALUES (999, "Mr_Garrison's_Penis", "Mrs. Garrison", "Who needs a penis?!", "I'm tired of men! I'm throwing this product away. Actually, can I have it back?", 5.0);

-- UPDATE averageReviews SET avgReview = 5.0 WHERE productID = 999;

-- UPDATE userReviews SET productName = "Mr_Garrisons_Penis" WHERE productID = 999;

-- SELECT reviewerName, reviewTitle, reviewBody, rating FROM userReviews WHERE productID = 999;

-- SELECT reviewerName FROM userReviews WHERE productID = 999;

-- SELECT reviewTitle FROM userReviews WHERE productID = 999;

-- SELECT reviewBody FROM userReviews WHERE productID = 999;

-- SELECT rating FROM userReviews WHERE productID = 999;