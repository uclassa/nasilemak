# Description
This repository contains a docker image that allows running streamlit web application.
 
# Development Usage
## Build the container
```bash
docker build -t ssa_admin_page .
```

## Run the container and mount the source code
```bash
docker run -d --name admin_page -p 8501:8501 -v $PWD/src:/src ssa_admin_page:latest
```

### After making changes to the source code, you must restart the container to view changes
```bash
docker restart admin_page
```

**View the app at:** http://localhost:8501

