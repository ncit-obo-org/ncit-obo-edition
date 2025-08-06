# NCIt OBO Edition

This project aims to develop an [OBO Library](http://obofoundry.org)-friendly release of the [NCI Thesaurus](https://ncit.nci.nih.gov/ncitbrowser/). Goals include adopting OBO conventions for term identifiers and ontology dereferencing, as well as improved semantic integration with existing OBO ontologies.

## Download

The OBO edition is a work in progress, so ontology content may change frequently. The in-progress ontology is available here: http://purl.obolibrary.org/obo/ncit.owl

## Release process for Developers

1. Enter `src/ontology` directory
1. Build the docker image to get all the tools together (alternatively, install the tools locally, see top of `Makefile`)
1. Run the make build process
1. Deploy the release on GitHub. Make sure the `GHVERSION` starts with a lower case `v` and corresponds to the exact date the build process above was run.

```
cd src/ontology
make docker-build
sh odk.sh make all -B
make deploy_release GHVERSION=v2022-08-19
```

**Notes on the above**:

Last time I tried this I was working on a system where I could not easily install `gh`. This is a workaround:

```
./odk.sh bash # Go inside ODK
gh auth login # Login with authentication token
git config --global --add safe.directory /work #This may be necessary if you do not have the correct access rights
make deploy_release GHVERSION=v2023-10-19 #(the usual)
```

## OBO Compliance

The contents of this ontology have been modified to comply with [OBO guidelines](https://obofoundry.org/docs/COC.html).

## Contact

Please use the [issue tracker](https://github.com/ncit-obo-org/ncit-obo-edition/issues) for providing feedback.
