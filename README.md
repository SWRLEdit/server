# SWRLEdit Server
The backend server for the SWRLEdit dashboard.

## Using

Start by building the docker image,

`docker build -t swrlserver .`

Run the image and expose port 8081 with

`docker run --name swrlapi -p 80:8081 swrlserver`

Visit `http://localhost:8081/` and confirm `http://localhost:8081/docs` renders.

## Development

New code should use reasonable syntax, conforming to PEP8 convention. New classes should be placed in new files and along with new associated unit test files.

### Tests
Tests should be added for new code and the project should maintain a good test coverage percentage (90%).

To run the tests, run `python3 -m pytest` from the root directory.
