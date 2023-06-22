/*
This Script is used when there is a need to fire a dynamic impression from within the creative

REQUIREMENT:
In order for all the macros to be replaced, it must be used in conjuction with 

*/
var imp_tracker_arr=[];
var macros_arr=[
	["[%siteName%]",		"myFT.get('siteName')"],
	["[%placementName%]",	"myFT.get('placementName')"],
	["[%creativeName%]",	"myFT.get('creativeName')"],
	["[%campaignName%]",	"myFT.get('campaignName')"],
	["[%thirdPartyID%]",	"myFT.get('thirdPartyID')"],
	["[FT_TIMESTAMP]",		"myFT.get('FT_TIMESTAMP')"],
	["[%FT_PROTOCOL%]",		"myFT.get('FT_PROTOCOL')"],
	["[%FT_RANDOM%]",		"Math.floor(Math.random() * 1e7)"],
	["[%placementWidth%]",	"myFT.manifestProperties.width"],
	["[%placementHeight%]",	"myFT.manifestProperties.height"],
	["[%campaignID%]",		"myFT.get('cID')"],
	["[%siteID%]",			"myFT.get('siteID')"],
	["[%placementID%]",		"myFT.get('pID')"],
	["[%creativeID%]",		"myFT.get('creativeID')"],
	["[%FT_CONFID%]",		"myFT.placementProperties.confID"],
	["[%FT_GDPR%]",			"myFT.get('FT_GDPR')"],
	["[%FT_GDPR_CONSENT%]",	"myFT.get('FT_GDPR_CONSENT')"]
]

	//ADD FT_SECTION AND FT_CUSTOM TO THE LIST

function replaceMacros (theURL) {
		
	var _theURL = theURL;
	
	for( var i = 0; i < macros_arr.length; i++ ){
		try{				
			_theURL = _theURL.replace( macros_arr[i][0], eval(macros_arr[i][1]) );
		}catch(err){
			console.log( "replace err:" + err );
		}
	 	
	}				 

	if ( theURL === myFT.instantAds.clickTag1_url ){
		myFT.instantAds.clickTag1_url = _theURL;
	} else {
		var img = new Image();
		img.src = _theURL;
	}
}
	
myFT.on('instantads', function(){			
	
	// 1) FIND ALL INSTANT AD VARIABLES WITH NAMES CONTAINING "impression_tracker" 
	
	// 2) PUSH 'impression_tracker' IA VARS INTO ARRAY 'imp_tracker_arr[]'

    for ( key in myFT.instantAds ) { 
        if( key.indexOf("impression_tracker") > -1 ) 
            imp_tracker_arr.push( myFT.instantAds[key] ); 
    }		
	// 3) REMOVE/TRIM WHITESPACE BEFORE AND AFTER EACH MACRO IN IMPRESSION URL
	for( i = 0; i < imp_tracker_arr.length; i++ ){		
		imp_tracker_arr[i] = imp_tracker_arr[i].trim();				
	// 4) REPLACE MACROS IN URL'S ESTABLISHE AS INSTANTAD VARIABLES NAMED 'impression_tracker_#'
		replaceMacros( imp_tracker_arr[i] );
	}

	// 5) REPLACE MACROS IN DYNAMIC URL
	replaceMacros( myFT.instantAds.clickTag1_url );
})