Feature: New Blog Post
    As a user of TDDBlogs,
    I want to create a blog post with a title and a content
    In order to publish it

    Scenario: User creates a blog with a title and a content
	    Given I go to the blog creation page
	    Given I fill the blogs title with "BDD rocks!"
	    Given I fill the blogs content with "So does Lettuce"
	    When I submit my blog
	    Then I should see a thank you page 
     
    