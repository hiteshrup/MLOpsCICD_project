from mlProject.config.configuration import DataValidationConfig 
import pandas as pd

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config
    
    def validate_all_columns(self)-> bool:
        try:
            validation_status = None
            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)

            all_schema = self.config.all_schema.keys()
            missing_columns = []

            for col in all_cols:
                if col not in all_schema:
                    missing_columns.append(col)
                
            
            if len(missing_columns) > 0:
                validation_status = False
                with open(self.config.STATUS_FILE, 'w') as f:
                    f.write(f"Validation status: {validation_status}, missing columns={missing_columns}")
            else:
                validation_status = True
                with open(self.config.STATUS_FILE, 'w') as f:
                    f.write(f"Validation status: {validation_status}")

                
            return validation_status
        
        except Exception as e:
            raise e