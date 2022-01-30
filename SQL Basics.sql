--USE DatabaseName;

DECLARE @ReportDate Date,@StartDate Date,@EndDate Date	
--SET @StartDate = DATEADD(DAY,1,EOMONTH(GETDATE(), -1))						    --FIRST DAY OF CURRENT MONTH
--SET @EndDate = DATEADD(MM,1,EOMONTH(GETDATE(), -1))								--LAST DAY OF CURRENT MONTH
--SET @StartDate = CAST(DATEADD(mm, DATEDIFF(mm, 0, (GETDATE())) -1,0) AS DATE)		--FIRST DAY OF PRIOR MONTH
--SET @EndDate = DATEADD(MM,0,EOMONTH(GETDATE(), -1))								--LAST DAY OF PRIOR MONTH
SET @StartDate = CASE WHEN DATEPART(WEEKDAY,CAST(GETDATE() AS DATE)) = 2			--DAILY RUN LOOKING AT YESTERDAY
					  THEN CAST(DATEADD(d, -3, GETDATE()) AS DATE)					--IF MONDAY, THEN GRAB FRIDAY'S DATE
					  ELSE CAST(DATEADD(d, -1, GETDATE()) AS DATE)					--IF NOT MONDAY, THEN GRAB YESTERDAY
					  END
SET @EndDate = CASE WHEN DATEPART(WEEKDAY,CAST(GETDATE() AS DATE)) = 2			--DAILY RUN LOOKING AT YESTERDAY
					  THEN CAST(DATEADD(d, -1, GETDATE()) AS DATE)					--IF MONDAY, THEN GRAB SUNDAY'S DATE
					  ELSE CAST(DATEADD(d, -1, GETDATE()) AS DATE)
                                END                                     					--IF NOT MONDAY, THEN GRAB YESTERDAY
--SET @Name = CAST(DATEADD(d, -1, GETDATE()) AS DATE)							--YESTERDAY

--SET @StartDate = '2022-01-11'
--SET @EndDate = '2022-01-11'

SELECT
DATEFROMPARTS(YEAR(HTR.TransactionPostDate),MONTH(HTR.TransactionPostDate),1)            POST_MONTH
,HTR.TransactionPostDate											REPORT_DATE		--IS THIS POST DATE IN FILE?
,''																SERVICE_MONTH
,''																SUM_DAYS_TO_PAY

,CASE
      WHEN HTR.FACILITYPREFIX = '2403' THEN 'Richmond'
      ELSE HTR.FACILITYNAME 
      END																			MARKET


,CASE WHEN HAR.PrimaryFinancialClass <> 'Self-pay' AND (HTR.FinancialClass = 'Self-pay' OR HTR.FinancialClass IS NULL) THEN 'SPAI'
	  WHEN HTR.FinancialClass = 'Self-pay' OR HTR.FinancialClass IS NULL THEN 'Self-Pay'
	  WHEN (HTR.FinancialClass <> 'Self-pay' OR HTR.FinancialClass IS NOT NULL) THEN HTR.FinancialClass
	  ELSE '' END												FC_ON_PMT


,CASE WHEN HAR.PrimaryFinancialClass <> 'Self-pay' AND (HTR.FinancialClass = 'Self-pay' OR HTR.FinancialClass IS NULL) THEN 'SPAI'
	  WHEN HTR.FinancialClass = 'Self-pay' OR HTR.FinancialClass IS NULL THEN 'SP'
	  WHEN (HTR.FinancialClass <> 'Self-pay' OR HTR.FinancialClass IS NOT NULL) THEN 'INS'
	  ELSE '' END												PMT_GROUP


,CASE WHEN HTR.FacilityPrefix IN ('3500','3501','3502') 
			AND (HTR.FinancialClass = 'Self-pay' OR HTR.FinancialClass IS NULL)
			AND (HAR.AdmitDate = '1900-01-01' OR HAR.AdmitDate IS NULL
				OR (DATEDIFF(DAY,HAR.AdmitDate,HTR.TransactionPostDate) < 8 OR DATEDIFF(DAY,HAR.DischargeDate,HTR.TransactionPostDate) < 8      
				AND DATEDIFF(DAY,HAR.AdmitDate,HTR.TransactionPostDate) > -60)) THEN 'POS'
		WHEN PTIQ.PTIQ_TRANS_ID IS NOT NULL  THEN 'PTIQ'
		ELSE '' END															 AS POS_FLAG




FROM [stg].[transaction_table]		HTR WITH (NOLOCK)
LEFT JOIN [stg].[demographic_info_table]	HAR WITH (NOLOCK)	ON HAR.AccountNumber = HTR.AccountNumber
LEFT JOIN [stg].[guarantor_information]    EAR WITH (NOLOCK)   ON EAR.ACCOUNTNUMBER = HTR.ACCOUNTNUMBER
-----------------FOR POST SERVICE POS PAYMENTS (PS-POS)--------------------
 LEFT OUTER JOIN (SELECT * FROM (
	SELECT
		SP.MedicalRecordNumber
		,VIS.AccountNumber							ACCT_NUM_NEW_ENC
		,CAST(VIS.AdmitDate AS DATE)				ADM_DT_NEW_ENC
		,SP.AccountNumber							ACCT_WITH_PMT
		,SP.PostDate								PTIQ_POST_DATE
		,SP.TransactionAmount						PTIQ_PMT_AMT
		,SP.TRANSACTIONID							PTIQ_TRANS_ID
		,ROW_NUMBER () OVER(PARTITION BY SP.TRANSACTIONID 
			ORDER BY VIS.ADMITDATE ASC)				AS	ROWNUMBER
	FROM			
		(SELECT
			HTR.AccountNumber
			,HTR.FacilityPrefix
			,PAT.MedicalRecordNumber
			,CAST(HTR.TransactionPostDate AS DATE)					PostDate
			,HTR.TransactionAmount
			,HTR.TransactionID
		FROM [stg].[transaction_table]					HTR		WITH (NOLOCK)
			LEFT OUTER JOIN [stg].[demographic_info_table]		PAT		WITH (NOLOCK) ON PAT.ACCOUNTNUMBER = HTR.ACCOUNTNUMBER 
																AND HTR.FacilityPrefix = PAT.FacilityPrefix
			--LEFT JOIN [dbo].[InsCrosswalk] FC ON HTR.InsuranceName = FC.INSURANCENAME
		WHERE 1=1
			AND TransactionType = 'P' --(TransactionType = 'P' OR UPPER(TransactionDescription) like '%REFUND%') 
			AND HTR.TransactionPostDate >= @STARTDATE
			AND HTR.TransactionPostDate < DATEADD(DAY,1,@ENDDATE)
			AND (HTR.FINANCIALCLASS IN ('Self-pay') OR HTR.FinancialClass IS NULL)	--SELF PAY PAYMENTS	
			AND HTR.FacilityPrefix IN ('3500','3501','3502') --FILTER FOR JUST CAVALIER FACILITIES
		)							SP
		INNER JOIN 	[stg].[hb_demographics]			PAT		WITH (NOLOCK)	ON PAT.MedicalRecordNumber = SP.MedicalRecordNumber AND PAT.FacilityPrefix = SP.FacilityPrefix
		INNER JOIN 	[stg].[hb_demographics]			VIS		WITH (NOLOCK)	ON VIS.AccountNumber = PAT.AccountNumber
									AND VIS.FacilityPrefix = PAT.FacilityPrefix
									AND SP.PostDate >= DATEADD(DAY,0,CAST(VIS.AdmitDate AS DATE))
									AND SP.PostDate < DATEADD(DAY,8,CAST(VIS.AdmitDate AS DATE))
									AND SP.AccountNumber <> VIS.AccountNumber
											--NO UNAPPLIED ACCTS
	)S 
	WHERE S.ROWNUMBER = 1) 
PTIQ ON PTIQ.PTIQ_TRANS_ID = HTR.TRANSACTIONID


WHERE 1=1
AND TRANSACTIONPOSTDATE  >= @StartDate
AND TRANSACTIONPOSTDATE < DATEADD(day,1,@EndDate)
	

AND HTR.FacilityPrefix IN ('2403','2402','2405','2409','1500','1400','1600','1700','1701','1708','1710','1800','2420','3500','3501','3502', '3503') 
AND (TransactionType = 'PAYMENT'
	OR (TransactionType IN ('CREDIT ADJUSTMENT', 'DEBIT ADJUSTMENT')
	AND TransactionCode IN ('3008','3013','3020')))






