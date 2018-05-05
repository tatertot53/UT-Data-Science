
var otuURL = "http://127.0.0.1:5000/names";
var metaURL = "/metadata/" + sample_id;
var wfreqURL = `/wfreq/${sample}`
var pieURL = "/samples/" + sample_id;


function buildDropdown() {
    var myDropdown = document.getElementByClassName("dropdown-item");

    Plotly.d3.json("../names", function(error,data) {
    	console.log(data)
        if (error) return console.warn(error);

        for (i = 0; i < data.length; i++) {
            SampleName = data[i]
            var selDatasetItem = document.createElement("div");
            myDropdown.appendChild(selDatasetItem[i]);
            selDatasetItem.text = SampleName;
            selDatasetItem.value = SampleName;
        
        }
    }
)}
buildDropdown()


function renderTable(sample_id) {
	Plotly.d3.json(metaURL, function(error,sample_metadata) {
		if(error) return console.warn(error);
		var metadata_info = {
			"AGE":metadata_info.AGE[0],
            "BBTYPE":metadata_info.BBTYPE[0],
            "ETHNICITY":metadata_info.ETHNICITY[0],
            "GENDER":metadata_info.GENDER[0],
            "LOCATION":metadata_info.LOCATION[0],
            "SAMPLEID":metadata_info.SAMPLEID[0]
        }

        var Metadata=document.getElementById('metadata')
        var Age=document.getElementById('age')
        var BBType=document.getElementById('bbtype')
        var Ethnicity=document.getElementById('ethnicity')
        var Gender=document.getElementById('gender')
        var Location=document.getElementById('location')
        var SampleID=document.getElementById('sampleid')

        Age.innerHTML="Age: "+metadata_info.AGE[0]
        BBType.innerHTML="BBType: "+metadata_info.BBTYPE[0]
        Ethnicity.innerHTML="Ethnicity: "+metadata_info.ETHNICITY[0]
        Gender.innerHTML="Gender: "+metadata_info.GENDER[0]
        Location.innerHTML="Location: "+metadata_info.LOCATION[0]
        SampleID.innerHTML="Sample ID: "+metadata_info.SAMPLEID[0]
		
	})
	
}

function updateResults(sample_id) {
	
	getMetadata(sample_id)
}


function getPieChartData(data) {
    console.log(data.samples)
    if (data.samples.length>10) {
        endListRange=9
        }
    else endListRange=data.samples.length-1

    top10Samples=[]
    top10OTUIDs=[]
    for (i = 0; i < endListRange; i++) {
        top10Samples.push(+data.samples[i])
        top10OTUIDs.push(+data.otu_id[i])
    }

    
    pieChartData = [{
        "labels": top10OTUIDs,
        "values": top10Samples,
        "type": "pie"}]

    return pieChartData
    
}



function pieChart(sample_id) {
	Plotly.d3.json(pieURL, function(error, data) {
		if(error) return console.warn(error);
		var layout = {
			title: "PIE!"}
		varPIE = document.getElementById('pie');

		var trace = getPieData(data)

		plotly.plot(PIE, trace, layout);
		})
}

pieChart('BB_940')


f

function buildPlot(sampleID) {
    url = '/samples/'+sampleID
    Plotly.d3.json(url, function(error, response) {

        console.log(response.samples);
        var trace1 = {
            x: response.otu_id,
            y: response.samples,
            mode: 'markers',
            marker: {
                size: response.samples,
                colorscale: 'Rainbow',
                color: response.otu_id,
                text: "sup"
            }
        };

        var data = [trace1];
      
        var layout = {
            title: "Bubble Size", 
            height: 600,
            width: 1000
            };
        
        var PLOT = document.getElementById('plot');
        Plotly.newPlot(PLOT, data, layout);
    });
}

buildPlot('BB_940');