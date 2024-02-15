-- Standardize the ProviderName column by trimming white spaces and setting to title case
UPDATE providers
SET ProviderName = INITCAP(TRIM(ProviderName));

-- Fill in missing values for YearsOfExperience with the average of the column
UPDATE providers
SET YearsOfExperience = (SELECT AVG(YearsOfExperience) FROM providers)
WHERE YearsOfExperience IS NULL;

-- Fix negative values in YearsOfExperience
UPDATE providers
SET YearsOfExperience = ABS(YearsOfExperience)
WHERE YearsOfExperience < 0;

-- Standardize the Location column to title case
UPDATE providers
SET Location = INITCAP(Location);

-- Correct the PatientSatisfactionScore values that are out of range (0-10)
-- Assuming scores should be within 1 to 10
UPDATE providers
SET PatientSatisfactionScore = NULL
WHERE PatientSatisfactionScore < 1 OR PatientSatisfactionScore > 10;

-- Remove duplicate records, keeping the one with the lowest ProviderID (as an example)
DELETE FROM providers
WHERE ProviderID NOT IN (
    SELECT MIN(ProviderID)
    FROM providers
    GROUP BY ProviderName, Specialization, Location
);

-- Correct the TreatmentCost formatting issues and outliers
-- Let's assume any treatment cost above a certain threshold is an outlier
UPDATE providers
SET TreatmentCost = NULL
WHERE TreatmentCost > 10000; -- This threshold would depend on domain knowledge

-- Normalize Specialization entries to ensure consistency
UPDATE providers
SET Specialization = 'General Practice'
WHERE Specialization IN ('GP', 'gen practice', 'general'); -- Example replacements

-- You might need to perform more complex cleaning depending on the data errors

-- Prepare the data for analysis and ML by selecting clean and relevant columns
SELECT
    ProviderID,
    ProviderName,
    Specialization,
    YearsOfExperience,
    Location,
    PatientRecoveryTime,
    PatientSatisfactionScore,
    TreatmentCost,
    SuccessfulTreatments,
    PatientVolume,
    FacilityRating
FROM providers
WHERE
    YearsOfExperience IS NOT NULL AND
    PatientRecoveryTime IS NOT NULL AND
    TreatmentCost IS NOT NULL AND
    PatientSatisfactionScore IS NOT NULL;
