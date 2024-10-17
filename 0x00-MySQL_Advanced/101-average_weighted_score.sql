-- Create stored procedure ComputeAverageWeightedScoreForUsers
DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    UPDATE users u
    SET average_score = (
        SELECT SUM(c.score * p.weight) / SUM(p.weight)
        FROM corrections c
        INNER JOIN projects p ON c.project_id = p.id
        WHERE c.user_id = u.id
    );
END //
DELIMITER ;
