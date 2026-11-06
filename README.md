these were meeting notes for OAP
This meeting scheduled to discuss on Flexwork Portal connections to establish with Cirrus Alpha and Master environments.
 
Decisions
Prioritize Alpha integration before master
Align all member data in one environment
Jeff's team: document endpoints by November 10 if feasible
Complete environment readiness by December 1
Open questions
Resolve test-to-Alpha versus stage-to-master mapping
Confirm One Portal integration with Yogesh
Agenda
Flexwork Portal environment connections (30 min)
Meeting notes
Portal Integration
Gomathi explained that FlexWork requests would come through a separate portal rather than the current USP process, and that Fulfillment would need to integrate with the portal to consume and process those requests
Gomathi requested clarification on which FlexWork environment or portal would connect to Alpha and which would connect to Master so the details could be documented for development work
The participants discussed confirming how the separate Alpha and development environments would connect and how each environment could point back to the other system
Chandra said the team needed to identify the interfaces integrating with Cirrus before deciding which environment and portal would connect to the applications and which would serve as the master; the interfaces would then be integrated accordingly
Jeff reported that the team had onboarded to the Nimbus APIs and was using ad hoc queries to understand the data while developers began building the integrations
Chandra said the team already had established connections with EMP and EPMP
Jeff said the portal was already fully integrated and functioning in test, stage, and production, with most remaining integration work occurring in the data integration layer; he also clarified that the team did not have a development environment and would work on live integrations in test
Gomathi explained that Surest had a new portal called One Portal that was not using UCC, and Chandra noted that the connection needed further discussion
Environment Integration
Chandra explained that USP Cirrus used Alpha for system integration testing and Master for end-to-end and UAT testing, and that both environments were intended for cross-application integration
Chandra clarified that member, claims, and fulfillment data would be kept in the same environment to support a consistent testing experience
Jeff explained that testing would be difficult if member eligibility, claims, benefits, and accumulator data were spread across environments without overlapping member records
Vandana said Alpha was the priority environment because it was connected end-to-end with most of the application, contained the required data, and would receive and test Cirrus changes first; Master was lower priority
Jeff explained that the test environment was used for developers’ initial testing, UAT, and integrations, while stage was used for business sign-off in a more stable environment
Participants discussed whether the portal’s test environment should connect to Alpha and its stage environment to Master; Chandra explained that Alpha received immediate development changes for system integration testing, while Master contained settled, release-based code that could take at least two weeks to receive
Chandra clarified that the Cirrus Alpha connection should be coordinated with the relevant application test environments, including OBAPI and the OAP portal, with the teams cross-validating the correct endpoints
Jeff said the team would prioritize providing the connection details by the 10th but could not promise that date because of limited team availability
Vandana said the FlexWork end-to-end team needed the environments ready by December 1 for testing, and Gomathi indicated that development work was also needed to connect to the OAP portal
Test Data
Jeff noted that test ID-card data was often unavailable for Doc 360 integrations, so the team typically had to mock data to simulate it; he also said EPMP data was difficult to align with Delta data
Follow-up tasks
Task
	
Assigned to
	
Due date
	
Bucket


Document the team and environment connections and provide the correct endpoints for the Cirrus Alpha integrations (Jeff)
	
Haugstad, Jeff
	
Tue, Nov 10
	
To do


Schedule a call for November 11 to identify which team will work on the FlexWork environment readiness (Chandra)
	
Sadineni, Chandra S
	
Fri, Nov 6
	
To do


Check with Yogesh about the Surest One Portal connection and arrange a discussion (Chandra)
	
Sadineni, Chandra S
	
Fri, Nov 6
	
To do
 
 
Test
https://test-flexwork.uhc.com/member
Stage
https://stage-flexwork.uhc.com/member
