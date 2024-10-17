-- Create stored procedure ComputeAverageWeightedScoreForUser
DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(
    IN user_id INT
)
BEGIN
    DECLARE weighted_avg_score FLOAT;
    
    SELECT SUM(corrections.score * projects.weight) / SUM(projects.weight)
    INTO weighted_avg_score
    FROM corrections
    INNER JOIN projects ON corrections.project_id = projects.id
    WHERE corrections.user_id = user_id;
    
    UPDATE users
    SET average_score = weighted_avg_score
    WHERE id = user_id;
END //
DELIMITER ;
